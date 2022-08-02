## Introduction

With `c4-review` you can estimate your payout for contest given the judges spreadsheet.


----

## Usage

```
$ ./c4-review --help
```

```
usage: c4-review [-h] [-w [HANDLE]] csv_file [pot_size]

Takes judges review spreadsheet and provides stats. Estimates payout if you provide a handle

positional arguments:
  csv_file
  pot_size

options:
  -h, --help            show this help message and exit
  -w [HANDLE], --handle [HANDLE]
```

## Without payouts

```
$ ./c4-review test-data/putty.csv
```

```json
{
  "results": [
    {
      "handle": "hansfriese",
      "ids": [
        {
          "id": "M-05",
          "dups": 31
        },
        {
          "id": "M-01",
          "dups": 16
        },
        {
          "id": "M-01",
          "dups": 16
        },
        {
          "id": "M-12",
          "dups": 9
        },
        {
          "id": "M-12",
          "dups": 9
        },
        {
          "id": "H-02",
          "dups": 5
        },
        {
          "id": "H-04",
          "dups": 2
        }
      ],
      "fraction": 0.11339685901028715
    },
    {
      "handle": "hyh",
      "ids": [
        {
          "id": "M-05",
          "dups": 31
        },
        {
          "id": "M-01",
          "dups": 16
        },
        {
          "id": "M-15",
          "dups": 4
        },
        {
          "id": "H-04",
          "dups": 2
        }
      ],
      "fraction": 0.09337907875963182
    },
    {
      "handle": "minhquanym",
      "ids": [
        {
          "id": "M-07",
          "dups": 3
        },
        {
          "id": "H-02",
          "dups": 5
        },
        {
          "id": "M-15",
          "dups": 4
        },
        {
          "id": "H-03",
          "dups": 6
        }
      ],
      "fraction": 0.06702544406417535
    },
    {
      "handle": "berndartmueller",
      "ids": [
        {
          "id": "M-05",
          "dups": 31
        },
        {
          "id": "H-01",
          "dups": 7
        },
        {
          "id": "M-10",
          "dups": 15
        },
        {
          "id": "M-11",
          "dups": 13
        },
        {
... continued ...
```

## With payouts

```
$ ./c4-review test-data/putty.csv 42500
```

```json
{
  "results": [
    {
      "handle": "hansfriese",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        },
        {
          "id": "H-02",
          "dups": 5,
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "H-04",
          "dups": 2,
          "payoutPerDup": "$3,508.97"
        }
      ],
      "fraction": 0.11339685901028715,
      "payout": "$4,819.37"
    },
    {
      "handle": "hyh",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-15",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "H-04",
          "dups": 2,
          "payoutPerDup": "$3,508.97"
        }
      ],
      "fraction": 0.09337907875963182,
      "payout": "$3,968.61"
    },
    {
      "handle": "minhquanym",
      "ids": [
        {
          "id": "M-07",
          "dups": 3,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "H-02",
          "dups": 5,
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "M-15",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.06702544406417535,
      "payout": "$2,848.58"
    },
    {
      "handle": "berndartmueller",
... continued ...
```

## Filter by warden
```
$ ./c4-review test-data/putty.csv 42500 -w sseefried
```

```json
{
  "results": [
    {
      "handle": "sseefried",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-08",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.016132606925043428,
      "payout": "$685.64"
    }
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```
