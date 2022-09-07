# `c4-review`

## Show your appreciation

If you like this tool please let me know [here](https://github.com/code-423n4/backstage-tools/issues/1) by giving me a reaction 👍 👎 ❤️ 👀 🚀.


## Introduction

With `c4-review` you can:
- see a summary of the findings with duplicate counts and a list of handles that found each issue
- estimate your contest payout given the Judge's Review spreadsheet.

Just export the Google Spreadsheet as a CSV file and try out one of the commands below.

For even prettier output just pipe the command into the `jq` tool.

e.g.

```
$ ./c4-review payouts test-data/putty.csv 42500 | jq
```

----

## Usage

### Commands

```
$ ./c4-review --help
```

```
usage: c4-review [-h] {payouts,findings} ...

Takes judges review spreadsheet and provides stats. Estimates payout if you provide a handle

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
usage: c4-review findings [-h] csv_file [pot_size]

Summary of findings, including duplicate counts

positional arguments:
  csv_file
  pot_size

options:
  -h, --help  show this help message and exit
```
### `payouts` command

```
$ ./c4-review payouts --help
```

```
usage: c4-review payouts [-h] [-w [HANDLE]] csv_file [pot_size]

Find out the fraction of total pot or payouts

positional arguments:
  csv_file
  pot_size

options:
  -h, --help            show this help message and exit
  -w [HANDLE], --handle [HANDLE]
```

## Findings summary

```
$ ./c4-review findings test-data/putty.csv 42500
```

```json
{
  "totalShares": 55.257356918267334,
  "findings": [
    {
      "id": "H-01",
      "dups": 7,
      "leadFinding": "zishansami",
      "handles": [
        "0x52",
        "0xsanson",
        "auditor0517",
        "berndartmueller",
        "csanuragjain",
        "zishansami",
        "zzzitron"
      ],
      "githubIssueId": "269",
      "sharesForIssue": 5.3144100000000005,
      "sharesPerDup": 0.7592014285714287,
      "fractionPerDup": 0.013739372834903852,
      "payoutPerDup": "$583.92"
    },
    {
      "id": "H-02",
      "dups": 5,
      "leadFinding": "kirk-baird",
      "handles": [
        "csanuragjain",
        "hansfriese",
        "kirk-baird",
        "Lambda",
        "minhquanym"
      ],
      "githubIssueId": "44",
      "sharesForIssue": 6.561,
      "sharesPerDup": 1.3122,
      "fractionPerDup": 0.023747064159093077,
      "payoutPerDup": "$1,009.25"
    },
    {
      "id": "H-03",
      "dups": 6,
      "leadFinding": "zzzitron",
      "handles": [
        "danb",
        "Kenshin",
        "Metatron",
        "minhquanym",
        "PwnedNoMore",
        "zzzitron"
      ],
      "githubIssueId": "369",
      "sharesForIssue": 5.9049000000000005,
      "sharesPerDup": 0.9841500000000001,
      "fractionPerDup": 0.01781029811931981,
      "payoutPerDup": "$756.94"
    },
    {
      "id": "H-04",
      "dups": 2,
      "leadFinding": "hyh",
      "handles": [
        "hansfriese",
        "hyh"
      ],
      "githubIssueId": "418",
      "sharesForIssue": 9.0,
      "sharesPerDup": 4.5,
      "fractionPerDup": 0.08143711988715047,
      "payoutPerDup": "$3,461.08"
    },
    {
      "id": "M-01",
      "dups": 14,
      "leadFinding": "kirk-baird",
      "handles": [
        "0xA5DF",
        "cccz",
        "chatch",
        "csanuragjain",
        "GalloDaSballo",
        "hansfriese",
        "hyh",
        "itsmeSTYJ",
        "Kenshin",
        "kirk-baird",
        "pedroais",
        "sashik_eth",
        "unforgiven",
        "xiaoming90"
      ],
      "githubIssueId": "50",
      "sharesForIssue": 0.7625597484987002,
      "sharesPerDup": 0.054468553464192875,
      "fractionPerDup": 0.0009857249152318088,
      "payoutPerDup": "$41.89"
    },
    {
      "id": "M-02",
      "dups": 5,
      "leadFinding": "IllIllI",
      "handles": [
        "0xNineDec",
        "IllIllI",
        "sashik_eth",
        "shung",
        "xiaoming90"
      ],
      "githubIssueId": "227",
      "sharesForIssue": 1.9683000000000002,
      "sharesPerDup": 0.39366,
      "fractionPerDup": 0.007124119247727923,
      "payoutPerDup": "$302.78"
    },
    {
      "id": "M-03",
      "dups": 4,
      "leadFinding": "IllIllI",
      "handles": [
        "0xNineDec",
        "exd0tpy",
        "IllIllI",
        "zzzitron"
      ],
      "githubIssueId": "223",
      "sharesForIssue": 2.1870000000000003,
      "sharesPerDup": 0.5467500000000001,
      "fractionPerDup": 0.009894610066288783,
      "payoutPerDup": "$420.52"
    },
    {
      "id": "M-04",
      "dups": 6,
      "leadFinding": "berndartmueller",
      "handles": [
        "0xsanson",
        "berndartmueller",
        "hubble",
        "Lambda",
        "Metatron",
        "swit"
      ],
      "githubIssueId": "285",
      "sharesForIssue": 1.7714700000000003,
      "sharesPerDup": 0.29524500000000004,
      "fractionPerDup": 0.005343089435795942,
      "payoutPerDup": "$227.08"
    },
    {
      "id": "M-05",
"... continued ..."
```

## Fractions for each handle

```
$ ./c4-review payouts test-data/putty.csv
```

```json
{
  "totalShares": 55.257356918267334,
  "payouts": [
    {
      "handle": "hansfriese",
      "findings": [
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088
        },
        {
          "id": "M-12",
          "dups": 8,
          "fractionPerDup": 0.003245926832246035
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08143711988715047
        }
      ],
      "fraction": 0.10954575478147785
    },
    {
      "handle": "hyh",
      "findings": [
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08143711988715047
        }
      ],
      "fraction": 0.09244737385642751
    },
    {
      "handle": "minhquanym",
      "findings": [
        {
          "id": "M-07",
          "dups": 3,
          "fractionPerDup": 0.014658681579687085
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783
        },
        {
          "id": "H-03",
          "dups": 6,
          "fractionPerDup": 0.01781029811931981
        }
      ],
      "fraction": 0.06611065392438875
    },
    {
      "handle": "csanuragjain",
      "findings": [
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013739372834903852
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088
        },
        {
          "id": "M-10",
          "dups": 15,
          "fractionPerDup": 0.0008280089287947194
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783
        }
      ],
      "fraction": 0.049194780904312244
    },
    {
      "handle": "berndartmueller",
      "findings": [
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668
        },
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013739372834903852
        },
        {
          "id": "M-10",
          "dups": 15,
          "fractionPerDup": 0.0008280089287947194
        },
        {
          "id": "M-11",
          "dups": 13,
          "fractionPerDup": 0.0011794998985679764
        },
        {
          "id": "M-04",
          "dups": 6,
          "fractionPerDup": 0.005343089435795942
        },
        {
          "id": "M-12",
          "dups": 8,
          "fractionPerDup": 0.003245926832246035
        },
"... continued ..."
```

## Payouts for each handle

```
$ ./c4-review payouts test-data/putty.csv 42500
```

```json
{
  "totalShares": 55.257356918267334,
  "payouts": [
    {
      "handle": "hansfriese",
      "findings": [
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077,
          "payoutPerDup": "$1,009.25"
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08143711988715047,
          "payoutPerDup": "$3,461.08"
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088,
          "payoutPerDup": "$41.89"
        },
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668,
          "payoutPerDup": "$5.52"
        },
        {
          "id": "M-12",
          "dups": 8,
          "fractionPerDup": 0.003245926832246035,
          "payoutPerDup": "$137.95"
        }
      ],
      "fraction": 0.10954575478147785,
      "payout": "$4,655.69"
    },
    {
      "handle": "hyh",
      "findings": [
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08143711988715047,
          "payoutPerDup": "$3,461.08"
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088,
          "payoutPerDup": "$41.89"
        },
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668,
          "payoutPerDup": "$5.52"
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783,
          "payoutPerDup": "$420.52"
        }
      ],
      "fraction": 0.09244737385642751,
      "payout": "$3,929.01"
    },
    {
      "handle": "minhquanym",
      "findings": [
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077,
          "payoutPerDup": "$1,009.25"
        },
        {
          "id": "H-03",
          "dups": 6,
          "fractionPerDup": 0.01781029811931981,
          "payoutPerDup": "$756.94"
        },
        {
          "id": "M-07",
          "dups": 3,
          "fractionPerDup": 0.014658681579687085,
          "payoutPerDup": "$622.99"
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783,
          "payoutPerDup": "$420.52"
        }
      ],
      "fraction": 0.06611065392438875,
      "payout": "$2,809.70"
    },
    {
      "handle": "csanuragjain",
      "findings": [
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013739372834903852,
          "payoutPerDup": "$583.92"
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.023747064159093077,
          "payoutPerDup": "$1,009.25"
        },
        {
          "id": "M-01",
          "dups": 14,
          "fractionPerDup": 0.0009857249152318088,
          "payoutPerDup": "$41.89"
        },
        {
          "id": "M-10",
          "dups": 15,
          "fractionPerDup": 0.0008280089287947194,
          "payoutPerDup": "$35.19"
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.009894610066288783,
          "payoutPerDup": "$420.52"
        }
      ],
      "fraction": 0.049194780904312244,
      "payout": "$2,090.78"
    },
    {
      "handle": "berndartmueller",
      "findings": [
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013739372834903852,
          "payoutPerDup": "$583.92"
        },
        {
          "id": "M-04",
"... continued ..."
```

## Payouts for specific warden
```
$ ./c4-review payouts test-data/putty.csv 42500 -w sseefried
```

```json
{
  "totalShares": 55.257356918267334,
  "payouts": [
    {
      "handle": "sseefried",
      "findings": [
        {
          "id": "M-05",
          "dups": 27,
          "fractionPerDup": 0.00012991898775645668,
          "payoutPerDup": "$5.52"
        },
        {
          "id": "M-08",
          "dups": 3,
          "fractionPerDup": 0.014658681579687085,
          "payoutPerDup": "$622.99"
        },
        {
          "id": "M-11",
          "dups": 13,
          "fractionPerDup": 0.0011794998985679764,
          "payoutPerDup": "$50.13"
        }
      ],
      "fraction": 0.015968100466011517,
      "payout": "$678.64"
    }
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```