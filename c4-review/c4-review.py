#!/usr/bin/env python3

import sys
import json
import argparse
import datetime
import os.path
import webbrowser
import requests

c4auth_login = os.getenv("C4AUTH_LOGIN")
if not c4auth_login:
  print("C4AUTH_LOGIN environment variable not found.")
  print("Grab yours by:")
  print("- logging in on the C4 website")
  print("- reading it via a cookie editor i.e. the 'Edit this cookie' Chrome extension")
  print("- and copying it to the C4AUTH_LOGIN environment variable")
  exit(1)

handles = {}
disputed_reports = set()

BASE = 0.85 # Base for Sybil protection. Was once 0.9 but 0.85 since Jul 2024

parser = argparse.ArgumentParser(prog="c4-review", formatter_class=argparse.RawTextHelpFormatter,
                                 description="Analyzes the C4 findings data and provides stats. Estimates payout if you provide a handle")
subp = parser.add_subparsers(dest="command") # dest="command" means that we see which command was parsed

base_help = f"Change base (default {BASE}) for Sybil protection e.g. --base=0.9 (for old comps)"

payout = subp.add_parser("payouts", description="Find out the fraction of total pot or payouts")
payout.add_argument('contest_slug', type=str)
payout.add_argument('pot_size', type=int, nargs='?')
payout.add_argument('-d', '--ignore_disputed', type=bool)
payout.add_argument('-w', '--handle', type=str, nargs='?')
payout.add_argument('-b', '--base', type=str, nargs=1, help=base_help)

open = subp.add_parser("open", description="Opens all findings from a given warden in browser")
open.add_argument('contest_slug', type=str)
open.add_argument('handle', type=str)

def get_findings(ns):
  headers = {
    "content-type": "application/json",
    "cookie": f"C4AUTH-LOGIN={os.getenv('C4AUTH_LOGIN')}"
  }

  findings = []

  page = 1
  last_page = 1

  while page <= last_page:
    # API change: findings moved behind submissions list; fetch submissions and rebuild finding aggregates
    url = f"https://code4rena.com/api/v1/audits/{ns.contest_slug}/submissions?perPage=100&page={page}"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
      try:
        body = resp.json()
      except Exception:
        body = resp.text
      print(f"Error fetching findings (HTTP {resp.status_code}) for page {page}.")
      print("Response:")
      print(body)
      print("Hint: Ensure C4AUTH_LOGIN is valid and the contest is accessible.")
      exit(1)

    try:
      response = resp.json()
    except Exception as e:
      print(f"Invalid JSON from API: {e}")
      print(resp.text[:500])
      exit(1)

    if not isinstance(response, dict) or 'data' not in response:
      print("Unexpected API response: missing 'data'. Full response below:")
      try:
        print(json.dumps(response, indent=2))
      except Exception:
        print(response)
      exit(1)

    # The submissions endpoint returns { data: { submissions: [...] }, pagination: {...} }
    data = response['data']
    subs = data['submissions'] if isinstance(data, dict) and 'submissions' in data else response['data']

    findings.extend(subs)
    last_page = response.get('pagination', {}).get('lastPage', last_page)
    page += 1

  # Transform submissions list into finding-like aggregates used by the rest of the script
  # Group by finding uid (or by (title, severity) if missing)
  by_finding = {}
  for sub in findings:
    finding_key = None
    if isinstance(sub, dict) and 'finding' in sub and isinstance(sub['finding'], dict):
      finding_key = sub['finding'].get('uid') or sub['finding'].get('number')
      finding_number = sub['finding'].get('number')
    else:
      finding_key = (sub.get('title'), sub.get('severity'))
      finding_number = None

    if finding_key not in by_finding:
      by_finding[finding_key] = {
        'uid': sub['finding'].get('uid') if isinstance(sub.get('finding'), dict) else None,
        'number': finding_number,
        'evaluations': [],
        'submissions': { 'data': [] },
        'duplicates': 0,
      }

    # Aggregate evaluations at finding level: collect all evaluation records with type in {validity,severity}
    for ev in (sub.get('evaluations') or []):
      if ev.get('type') in ['validity', 'severity']:
        by_finding[finding_key]['evaluations'].append(ev)

    # Add to submissions data with required shape
    sub_entry = {
      'number': sub.get('number'),
      'user': sub.get('user'),
      'team': sub.get('team'),
      'severity': sub.get('severity'),
      'evaluations': sub.get('evaluations') or [],
    }
    by_finding[finding_key]['submissions']['data'].append(sub_entry)

  # Compute duplicates (unique/partial count) as count of non-zero credit submissions; fallback to total submissions
  findings_list = []
  for f in by_finding.values():
    dups = 0
    for sub in f['submissions']['data']:
      credit = 1.0
      for ev in sub['evaluations']:
        if ev.get('type') == 'credit':
          try:
            credit = int(ev['value'][:-1]) / 100
          except Exception:
            credit = 1.0
      if credit > 0:
        dups += credit
    if dups == 0:
      dups = len(f['submissions']['data'])
    f['dups'] = dups
    findings_list.append(f)

  return findings_list

def pp_usd(n):
  return '${:0,.2f}'.format(round(n, 2))

def pp_month(epoch_time):
  dt = datetime.datetime.fromtimestamp(epoch_time)
  return dt.strftime("%B %Y")

def pp_time(epoch_time):
  dt = datetime.datetime.fromtimestamp(epoch_time)
  return dt.isoformat()

def is_high(finding_or_submission):
  return finding_or_submission["severity"].lower() == "high"

def get_credit(submission):
  quality = None
  credit = 1.0

  for evaluation in submission["evaluations"]:
    if evaluation["type"] == "quality":
      quality = evaluation["value"]
    elif evaluation["type"] == "credit":
      credit = int(evaluation["value"][:-1]) / 100

  if quality != "sufficient":
    return 0

  return credit

def get_validity_and_severity(finding):
  validity = None
  severity = finding["submissions"]["data"][0]["severity"]

  for evaluation in finding["evaluations"]:
    if evaluation["type"] == "validity" and evaluation["userAuditRole"] != "sponsor":
      validity = evaluation["value"]
    elif evaluation["type"] == "severity":
      severity = evaluation["value"]

  return (validity, severity)

def payout(ns):
  findings = get_findings(ns)

  ws = {}
  total_shares = 0

  for finding in findings:
    num_dups = 0
    validity, severity = get_validity_and_severity(finding)
    finding["severity"] = severity

    if validity != "valid" or severity not in ["high", "medium"]:
      continue

    for submission in finding["submissions"]['data']:
      credit = get_credit(submission)
      if credit == 0:
        continue

      num_dups += credit

    if num_dups == 0:
      continue

    base_shares = 10 if is_high(finding) else 3
    finding["shares"] = base_shares * BASE**(num_dups - 1) / num_dups
    finding["dups"] = num_dups
    total_shares += finding["shares"] * (num_dups + 0.3)


  # Summarise results for each handle
  for finding in findings:
    if "shares" not in finding:
      continue

    for idx, submission in enumerate(finding["submissions"]['data']):
      credit = get_credit(submission)
      if credit == 0:
        continue
    
      if idx == 0:
        submission["sliceCredit"] = 1.3
      else:
        submission["sliceCredit"] = credit
      
      submission["shares"] = finding["shares"] * submission["sliceCredit"]

      w = submission["user"]["handle"]
      if submission["team"] != None:
        w = f"{submission['team']['handle']} ({', '.join(sorted(m['handle'] for m in submission['team']['members']))})"
      if not w in ws:
        ws[w] = { "rank": 0, "handle": w }
        if ns.pot_size != None:
          ws[w]["payout"] = 0.0
        ws[w].update({ "findings": [], "findingsCount": 0, "fraction": 0.0 })

      rec = { 
        "submissionId" : "S-" + str(submission["number"]),
        "findingId": "F-" + str(finding["number"]),
        "isLeadSubmission": idx == 0,
        "severity": finding["severity"],
        "dups": finding["dups"],
        "sliceCredit": submission["sliceCredit"],
        "shares": submission["shares"]
      }
      ws[w]["findings"].append(rec)

      if ns.pot_size != None:
        rec["payout"] = ns.pot_size * 0.8 * rec["shares"] / total_shares
        ws[w]["payout"] += rec["payout"]

  for w in ws:
    ws[w]["findingsCount"] = len(ws[w]["findings"])
    ws[w]["findings"].sort(key=lambda r: -r["shares"])

  # Calculate bonuses
  gatherers, highest_gatherer_score = ([], 0)
  hunters, highest_hunter_score = ([], 0)
  num_highs = sum(finding["severity"] == "high" and "shares" in finding for finding in findings)
  num_mediums = sum(finding["severity"] == "medium" and "shares" in finding for finding in findings)

  for w in ws:
    gatherer_score = 0
    hunter_score = 0
    for f in ws[w]["findings"]:
      severity_score = 10 if is_high(f) else 3
      total_severity_findings = num_highs if is_high(f) else num_mediums
      # Only full-credit findings count towards TH/TG scoring, but partial credits affect duplicate count
      # (see https://docs.code4rena.com/awarding/incentive-model-and-awards#bonuses-for-top-competitors)
      if f["sliceCredit"] >= 1:
        gatherer_score += severity_score / total_severity_findings
        # Calculate effective number of duplicates including partial credits, remove bonus for selected
        effective_dups = sum(d["sliceCredit"] for d in dup_sets[f["leadFindingId"]]["findings"]) - 0.3
        if effective_dups < 5:
          hunter_score += severity_score / effective_dups

    ws[w]["gathererScore"] = gatherer_score
    if gatherer_score > highest_gatherer_score:
      highest_gatherer_score = gatherer_score
      gatherers = [w]
    elif gatherer_score == highest_gatherer_score:
      gatherers.append(w)

    ws[w]["hunterScore"] = hunter_score
    if hunter_score > highest_hunter_score:
      highest_hunter_score = hunter_score
      hunters = [w]
    elif hunter_score == highest_hunter_score:
      hunters.append(w)

  bonus = ns.pot_size * 0.1 if ns.pot_size != None else 0.1
  for role, winners in [("hunter", hunters), ("gatherer", gatherers)]:
    for winner in winners:
      ws[winner][f"{role}Bonus"] = round(bonus / len(winners), 2)
      if ns.pot_size != None:
        ws[winner]["payout"] += bonus / len(winners)

  # Prepare and format warden summaries for output
  warden_summaries = [ws[w] for w in ws if (lambda w: ns.handle == None or ns.handle in w)(w)]
  if ns.pot_size != None:
    warden_summaries.sort(key=lambda r: -r["payout"])
  else: # should be the same
    warden_summaries.sort(key=lambda r: -(r["fraction"] * 0.8 + r.get("hunterBonus", 0) + r.get("gathererBonus", 0)))

  for i in range(len(warden_summaries)):
    warden_summaries[i]['rank'] = i + 1
    if ns.pot_size != None:
      warden_summaries[i]['payout'] = round(warden_summaries[i]['payout'], 2)
      for finding in warden_summaries[i]['findings']:
        finding['payout'] = round(finding['payout'], 2)

  return { "totalShares": total_shares, "payouts": warden_summaries }

ns = parser.parse_args(sys.argv[1:])

#
# Set the base if the -b, --base flag is provided
# or the csv_file if it is provided
#
def set_base(base):
  global BASE
  if base != None:
    BASE = float(base[0])
  else:
    BASE = 0.85

if ns.command == "payouts":
  set_base(ns.base)
  result = payout(ns)
# elif ns.command == "open": TODO reintroduce
#   open(ns)
#   result = {}
else:
  parser.parse_args(["--help"])

result["note"] = ("This tool only calculates shares for Highs and Mediums. " +
                  "It does not take into account QA reports.")

## Prints the records as valid JSON
print(json.dumps(result, indent=2))
