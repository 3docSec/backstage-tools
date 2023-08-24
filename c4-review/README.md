# `c4-review`

## Show your appreciation

If you like this tool please let me know [here](https://github.com/code-423n4/backstage-tools/issues/1) by giving me a reaction 👍 👎 ❤️ 👀 🚀.


## Introduction

With `c4-review` you can:
- see a summary of the findings with duplicate counts and a list of handles that found each issue
- estimate your contest payout given the current status of the GitHub finding repo.

Just find out the findings repo name of the contest you look for and try out one of the commands below.

For even prettier output just pipe the command into the `jq` tool.

e.g.

```
$ ./c4-review payouts 2023-08-goodentry-findings 46000 | jq
```

----

## Installation
`c4-review` is an executable script you can run as a shell command. 

Before running it, you'll need to:
- install Python 3 if you haven't already
- install [PyGithub](https://github.com/PyGithub/PyGithub)
- generate [a GitHub access token](https://github.com/settings/tokens) with `repository` access
- set the token generated above to the `GITHUB_ACCESS_TOKEN` environment variable 

## Usage

### Commands

```
$ ./c4-review --help
```

```
usage: c4-review [-h] {payouts,findings} ...

Analyzes the GitHub findings repo and provides stats. Estimates payout if you provide a handle

positional arguments:
  {payouts,findings}

options:
  -h, --help          show this help message and exit
```
### `findings` command

```
$ ./c4-review findings --help
```

```
usage: c4-review findings [-h] findings_repo [pot_size]

Summary of findings, including duplicate counts

positional arguments:
  findings_repo
  pot_size

options:
  -h, --help  show this help message and exit
```
### `payouts` command

```
$ ./c4-review payouts --help
```

```
usage: c4-review payouts [-h] [-w [HANDLE]] findings_repo [pot_size]

Find out the fraction of total pot or payouts

positional arguments:
  findings_repo
  pot_size

options:
  -h, --help            show this help message and exit
  -w [HANDLE], --handle [HANDLE]
```

## Findings summary
Note: the below examples use data taken from an actual contest - [Amphora protocol](https://code4rena.com/contests/2023-07-amphora-protocol))

```
$ ./c4-review findings 2023-07-amphora-findings 46250
```

```json
{                                                                                                                                                                                 [60/25031]
  "totalShares": 32.48464550591162,
  "findings": [
    {
      "id": "233",
      "dups": 1,
      "leadFinding": "ljmanini",
      "handles": [
        "ljmanini"
      ],
      "severity": "M",
      "githubIssueId": "233",
      "sharesForIssue": 3.0,
      "sharesPerDup": 3.0,
      "fractionPerDup": 0.09235132331839835,
      "payoutPerDup": "$4,271.25"
    },
    {
      "id": "256",
      "dups": 19,
      "leadFinding": "giovannidisiena",
      "handles": [
        "josephdara",
        "mert_eren",
        "adeolu",
        "ak1",
        "pep7siup",
        "Bauchibred",
        "qpzm",
        "SanketKogekar",
        "said",
        "giovannidisiena",
        "Giorgio",
        "ljmanini",
        "Musaka",
        "SpicyMeatball",
        "0xbranded",
        "0xComfyCat",
        "0xWaitress",
        "erebus",
        "kutugu"
      ],
      "severity": "H",
      "githubIssueId": "256",
      "sharesForIssue": 1.5009463529699918,
      "sharesPerDup": 0.07899717647210483,
      "fractionPerDup": 0.002431831261871975,
      "payoutPerDup": "$112.47"
    },
    "... continued ..."
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```

## Fractions for each handle

```
$ ./c4-review payouts 2023-07-amphora-findings
```

```json
{
  "totalShares": 32.48464550591162,
  "payouts": [
    {
      "handle": "minhtrng",
      "findings": [
        {
          "id": "414",
          "dups": 1,
          "fractionPerDup": 0.09235132331839835,
          "isLeadFinding": true
        },
        {
          "id": "301",
          "dups": 2,
          "fractionPerDup": 0.13852698497759752,
          "isLeadFinding": false
        }
      ],
      "fraction": 0.25858370529151536
    },
    {
      "handle": "said",
      "findings": [
        {
          "id": "301",
          "dups": 2,
          "fractionPerDup": 0.13852698497759752,
          "isLeadFinding": true
        },
        {
          "id": "256",
          "dups": 19,
          "fractionPerDup": 0.002431831261871975,
          "isLeadFinding": false
        }
      ],
      "fraction": 0.18251691173274875
    },
    "... continued ..."
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```

## Payouts for each handle

```
$ ./c4-review payouts 2023-07-amphora-findings 46250
```

```json
{
  "totalShares": 32.48464550591162,
  "payouts": [
    {
      "handle": "minhtrng",
      "findings": [
        {
          "id": "301",
          "dups": 2,
          "fractionPerDup": 0.13852698497759752,
          "isLeadFinding": false,
          "payoutPerDup": "$6,406.87"
        },
        {
          "id": "414",
          "dups": 1,
          "fractionPerDup": 0.09235132331839835,
          "isLeadFinding": true,
          "payoutPerDup": "$4,271.25"
        }
      ],
      "fraction": 0.25858370529151536,
      "payout": "$11,959.50"
    },
    {
      "handle": "said",
      "findings": [
        {
          "id": "256",
          "dups": 19,
          "fractionPerDup": 0.002431831261871975,
          "isLeadFinding": false,
          "payoutPerDup": "$112.47"
        },
        {
          "id": "301",
          "dups": 2,
          "fractionPerDup": 0.13852698497759752,
          "isLeadFinding": true,
          "payoutPerDup": "$6,406.87"
        }
      ],
      "fraction": 0.18251691173274875,
      "payout": "$8,441.41"
    },
    "... continued ...",
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```

## Payouts for specific warden
```
$ ./c4-review payouts 2023-07-amphora-findings 46250 -w said
```

```json
{
  "totalShares": 32.48464550591162,
  "payouts": [
    {
      "handle": "said",
      "findings": [
        {
          "id": "256",
          "dups": 19,
          "fractionPerDup": 0.002431831261871975,
          "isLeadFinding": false,
          "payoutPerDup": "$112.47"
        },
        {
          "id": "301",
          "dups": 2,
          "fractionPerDup": 0.13852698497759752,
          "isLeadFinding": true,
          "payoutPerDup": "$6,406.87"
        }
      ],
      "fraction": 0.18251691173274875,
      "payout": "$8,441.41"
    }
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```