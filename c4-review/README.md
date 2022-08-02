# `c4-review`

## Introduction

With `c4-review` you can estimate your payout for contest given the judges spreadsheet. Just export the Google Spreadsheet as a CSV file and try out one of the commands below.

For even prettier output just pipe the command into the `jq` tool.

e.g.

```
$ ./c4-review test-data/putty.csv 42500 | jq
```


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
          "dups": 31,
          "leadFinding": "IllIllI",
          "handles": [
            "0x29A",
            "0xc0ffEE",
            "0xDjango",
            "AmitN",
            "auditor0517",
            "berndartmueller",
            "BowTiedWardens",
            "BowTiedWardens",
            "cccz",
            "danb",
            "dipp",
            "dirk_y",
            "hansfriese",
            "horsefacts",
            "hyh",
            "IllIllI",
            "joestakey",
            "kirk-baird",
            "oyc_109",
            "oyc_109",
            "oyc_109",
            "peritoflores",
            "rfa",
            "sashik_eth",
            "simon135",
            "sseefried",
            "StErMi",
            "swit",
            "xiaoming90",
            "xiaoming90",
            "zzzitron"
          ]
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
          ]
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
          ]
        },
        {
          "id": "M-12",
          "dups": 9,
          "leadFinding": "berndartmueller",
          "handles": [
            "auditor0517",
            "berndartmueller",
            "hansfriese",
            "hansfriese",
            "IllIllI",
            "Lambda",
            "sashik_eth",
            "shenwilly",
            "TrungOre"
          ]
        },
        {
          "id": "M-12",
          "dups": 9,
          "leadFinding": "berndartmueller",
          "handles": [
            "auditor0517",
            "berndartmueller",
            "hansfriese",
            "hansfriese",
            "IllIllI",
            "Lambda",
            "sashik_eth",
            "shenwilly",
            "TrungOre"
          ]
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
          ]
        },
        {
          "id": "H-04",
          "dups": 2,
          "leadFinding": "hyh",
          "handles": [
            "hansfriese",
            "hyh"
          ]
        }
      ],
      "fraction": 0.11339685901028715
    },
    {
      "handle": "hyh",
      "ids": [
        {
          "id": "M-05",
"... continued ..."
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
          "leadFinding": "IllIllI",
          "handles": [
            "0x29A",
            "0xc0ffEE",
            "0xDjango",
            "AmitN",
            "auditor0517",
            "berndartmueller",
            "BowTiedWardens",
            "BowTiedWardens",
            "cccz",
            "danb",
            "dipp",
            "dirk_y",
            "hansfriese",
            "horsefacts",
            "hyh",
            "IllIllI",
            "joestakey",
            "kirk-baird",
            "oyc_109",
            "oyc_109",
            "oyc_109",
            "peritoflores",
            "rfa",
            "sashik_eth",
            "simon135",
            "sseefried",
            "StErMi",
            "swit",
            "xiaoming90",
            "xiaoming90",
            "zzzitron"
          ],
          "payoutPerDup": "$3.20"
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
          "payoutPerDup": "$30.10"
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
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-12",
          "dups": 9,
          "leadFinding": "berndartmueller",
          "handles": [
            "auditor0517",
            "berndartmueller",
            "hansfriese",
            "hansfriese",
            "IllIllI",
            "Lambda",
            "sashik_eth",
            "shenwilly",
            "TrungOre"
          ],
          "payoutPerDup": "$111.89"
        },
        {
          "id": "M-12",
          "dups": 9,
          "leadFinding": "berndartmueller",
          "handles": [
            "auditor0517",
            "berndartmueller",
            "hansfriese",
            "hansfriese",
            "IllIllI",
            "Lambda",
            "sashik_eth",
            "shenwilly",
            "TrungOre"
          ],
          "payoutPerDup": "$111.89"
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
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "H-04",
          "dups": 2,
          "leadFinding": "hyh",
          "handles": [
            "hansfriese",
            "hyh"
          ],
          "payoutPerDup": "$3,508.97"
        }
      ],
"... continued ..."
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
          "leadFinding": "IllIllI",
          "handles": [
            "0x29A",
            "0xc0ffEE",
            "0xDjango",
            "AmitN",
            "auditor0517",
            "berndartmueller",
            "BowTiedWardens",
            "BowTiedWardens",
            "cccz",
            "danb",
            "dipp",
            "dirk_y",
            "hansfriese",
            "horsefacts",
            "hyh",
            "IllIllI",
            "joestakey",
            "kirk-baird",
            "oyc_109",
            "oyc_109",
            "oyc_109",
            "peritoflores",
            "rfa",
            "sashik_eth",
            "simon135",
            "sseefried",
            "StErMi",
            "swit",
            "xiaoming90",
            "xiaoming90",
            "zzzitron"
          ],
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-11",
          "dups": 13,
          "leadFinding": "Picodes",
          "handles": [
            "0xNineDec",
            "0xsanson",
            "antonttc",
            "berndartmueller",
            "BowTiedWardens",
            "catchup",
            "dirk_y",
            "GalloDaSballo",
            "horsefacts",
            "Metatron",
            "Picodes",
            "sseefried",
            "unforgiven"
          ],
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-08",
          "dups": 3,
          "leadFinding": "kirk-baird",
          "handles": [
            "kirk-baird",
            "reassor",
            "sseefried"
          ],
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



