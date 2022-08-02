# `c4-review`

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
./gen-docs.sh: line 43: findings: command not found
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
./gen-docs.sh: line 46: payouts: command not found
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

```
{
  "results": [
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
      "sharesForIssue": 5.3144100000000005,
      "sharesPerDup": 0.7592014285714287,
      "fractionPerDup": 0.013929488074281104,
      "payoutPerDup": "$592.00"
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
      "sharesForIssue": 6.561,
      "sharesPerDup": 1.3122,
      "fractionPerDup": 0.02407565839999203,
      "payoutPerDup": "$1,023.22"
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
      "sharesForIssue": 5.9049000000000005,
      "sharesPerDup": 0.9841500000000001,
      "fractionPerDup": 0.018056743799994023,
      "payoutPerDup": "$767.41"
    },
    {
      "id": "H-04",
      "dups": 2,
      "leadFinding": "hyh",
      "handles": [
        "hansfriese",
        "hyh"
      ],
      "sharesForIssue": 9.0,
      "sharesPerDup": 4.5,
      "fractionPerDup": 0.08256398628255154,
      "payoutPerDup": "$3,508.97"
    },
    {
      "id": "M-01",
      "dups": 16,
      "leadFinding": "kirk-baird",
      "handles": [
        "0xA5DF",
        "cccz",
        "cccz",
        "chatch",
        "csanuragjain",
        "GalloDaSballo",
        "hansfriese",
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
      "sharesForIssue": 0.6176733962839472,
      "sharesPerDup": 0.0386045872677467,
      "fractionPerDup": 0.0007082996919150672,
      "payoutPerDup": "$30.10"
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
      "sharesForIssue": 1.9683000000000002,
      "sharesPerDup": 0.39366,
      "fractionPerDup": 0.0072226975199976085,
      "payoutPerDup": "$306.96"
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
      "sharesForIssue": 2.1870000000000003,
      "sharesPerDup": 0.5467500000000001,
      "fractionPerDup": 0.010031524333330013,
      "payoutPerDup": "$426.34"
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
      "sharesForIssue": 1.7714700000000003,
      "sharesPerDup": 0.29524500000000004,
      "fractionPerDup": 0.005417023139998207,
      "payoutPerDup": "$230.22"
    },
    {
      "id": "M-05",
      "dups": 31,
      "leadFinding": "IllIllI",
      "handles": [
        "0x29A",
        "0xc0ffEE",
        "0xDjango",
        "AmitN",
"... continued ..."
```

## Fractions for each handle

```
$ ./c4-review payouts test-data/putty.csv
```

```json
{
  "results": [
    {
      "handle": "hansfriese",
      "findings": [
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672
        },
        {
          "id": "M-12",
          "dups": 9,
          "fractionPerDup": 0.0026326732460391286
        },
        {
          "id": "M-12",
          "dups": 9,
          "fractionPerDup": 0.0026326732460391286
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.02407565839999203
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08256398628255154
        }
      ],
      "fraction": 0.11339685901028715
    },
    {
      "handle": "hyh",
      "findings": [
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.010031524333330013
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08256398628255154
        }
      ],
      "fraction": 0.09337907875963182
    },
    {
      "handle": "minhquanym",
      "findings": [
        {
          "id": "M-07",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278
        },
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.02407565839999203
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.010031524333330013
        },
        {
          "id": "H-03",
          "dups": 6,
          "fractionPerDup": 0.018056743799994023
        }
      ],
      "fraction": 0.06702544406417535
    },
    {
      "handle": "berndartmueller",
      "findings": [
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05
        },
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013929488074281104
        },
        {
          "id": "M-10",
          "dups": 15,
          "fractionPerDup": 0.0008394663015289684
        },
        {
          "id": "M-11",
          "dups": 13,
          "fractionPerDup": 0.001195820942348958
        },
        {
          "id": "M-04",
          "dups": 6,
          "fractionPerDup": 0.005417023139998207
        },
        {
          "id": "M-12",
          "dups": 9,
          "fractionPerDup": 0.0026326732460391286
        },
        {
          "id": "M-06",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278
        },
        {
          "id": "M-06",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278
        }
      ],
      "fraction": 0.05381277521775012
    },
    {
      "handle": "csanuragjain",
      "findings": [
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013929488074281104
        },
        {
"... continued ..."
```

## Payouts for each handle

```
$ ./c4-review payouts test-data/putty.csv 42500
```

```json
{
  "results": [
    {
      "handle": "hansfriese",
      "findings": [
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.02407565839999203,
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08256398628255154,
          "payoutPerDup": "$3,508.97"
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-12",
          "dups": 9,
          "fractionPerDup": 0.0026326732460391286,
          "payoutPerDup": "$111.89"
        },
        {
          "id": "M-12",
          "dups": 9,
          "fractionPerDup": 0.0026326732460391286,
          "payoutPerDup": "$111.89"
        }
      ],
      "fraction": 0.11339685901028715,
      "payout": "$4,819.37"
    },
    {
      "handle": "hyh",
      "findings": [
        {
          "id": "H-04",
          "dups": 2,
          "fractionPerDup": 0.08256398628255154,
          "payoutPerDup": "$3,508.97"
        },
        {
          "id": "M-01",
          "dups": 16,
          "fractionPerDup": 0.0007082996919150672,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.010031524333330013,
          "payoutPerDup": "$426.34"
        }
      ],
      "fraction": 0.09337907875963182,
      "payout": "$3,968.61"
    },
    {
      "handle": "minhquanym",
      "findings": [
        {
          "id": "H-02",
          "dups": 5,
          "fractionPerDup": 0.02407565839999203,
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "H-03",
          "dups": 6,
          "fractionPerDup": 0.018056743799994023,
          "payoutPerDup": "$767.41"
        },
        {
          "id": "M-07",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "M-15",
          "dups": 4,
          "fractionPerDup": 0.010031524333330013,
          "payoutPerDup": "$426.34"
        }
      ],
      "fraction": 0.06702544406417535,
      "payout": "$2,848.58"
    },
    {
      "handle": "berndartmueller",
      "findings": [
        {
          "id": "H-01",
          "dups": 7,
          "fractionPerDup": 0.013929488074281104,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-04",
          "dups": 6,
          "fractionPerDup": 0.005417023139998207,
          "payoutPerDup": "$230.22"
        },
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-06",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "M-06",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "M-10",
          "dups": 15,
          "fractionPerDup": 0.0008394663015289684,
"... continued ..."
```

## Payouts for specific warden
```
$ ./c4-review payouts test-data/putty.csv 42500 -w sseefried
```

```json
{
  "results": [
    {
      "handle": "sseefried",
      "findings": [
        {
          "id": "M-05",
          "dups": 31,
          "fractionPerDup": 7.526845183519193e-05,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-08",
          "dups": 3,
          "fractionPerDup": 0.014861517530859278,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "M-11",
          "dups": 13,
          "fractionPerDup": 0.001195820942348958,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.016132606925043428,
      "payout": "$685.64"
    }
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```





