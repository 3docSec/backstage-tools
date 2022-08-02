## Introduction

With `c4-review` you can estimate your payout for contest given the judges spreadsheet.


----

## Usage

```
$ ./c4-review --help
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
Traceback (most recent call last):
  File "/home/sseefried/code/codearena/backstage-tools/c4-review/./c4-review", line 143, in <module>
    result=run(ns)
  File "/home/sseefried/code/codearena/backstage-tools/c4-review/./c4-review", line 97, in run
    ws[w]["ids"].append({ "id": id, "dups": h[id]["dups"], "payoutPerDup": ppUSD(h[id]["payoutPerDup"])})
KeyError: 'payoutPerDup'
```

## With payouts

```
$ ./c4-review test-data/putty.csv 42500
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
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        },
        {
          "id": "M-06",
          "dups": 3,
          "payoutPerDup": "$631.61"
        },
        {
          "id": "M-06",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.05381277521775012,
      "payout": "$2,287.04"
    },
    {
      "handle": "csanuragjain",
      "ids": [
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
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
        }
      ],
      "fraction": 0.04958443680104718,
      "payout": "$2,107.34"
    },
    {
      "handle": "zzzitron",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-03",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.04209302465944033,
      "payout": "$1,788.95"
    },
    {
      "handle": "unforgiven",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-09",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-14",
          "dups": 2,
          "payoutPerDup": "$1,052.69"
        }
      ],
      "fraction": 0.04180923781247186,
      "payout": "$1,776.89"
    },
    {
      "handle": "kirk-baird",
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
          "id": "H-02",
          "dups": 5,
          "payoutPerDup": "$1,023.22"
        },
        {
          "id": "M-08",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.03972074407460156,
      "payout": "$1,688.13"
    },
    {
      "handle": "horsefacts",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-09",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-16",
          "dups": 2,
          "payoutPerDup": "$1,052.69"
        }
      ],
      "fraction": 0.03904374124310029,
      "payout": "$1,659.36"
    },
    {
      "handle": "IllIllI",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-02",
          "dups": 5,
          "payoutPerDup": "$306.96"
        },
        {
          "id": "M-03",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        },
        {
          "id": "M-07",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.03566314738359019,
      "payout": "$1,515.68"
    },
    {
      "handle": "Lambda",
      "ids": [
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
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
        }
      ],
      "fraction": 0.03212535478602936,
      "payout": "$1,365.33"
    },
    {
      "handle": "shung",
      "ids": [
        {
          "id": "M-02",
          "dups": 5,
          "payoutPerDup": "$306.96"
        },
        {
          "id": "M-14",
          "dups": 2,
          "payoutPerDup": "$1,052.69"
        }
      ],
      "fraction": 0.03199189340476307,
      "payout": "$1,359.66"
    },
    {
      "handle": "hubble",
      "ids": [
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
        },
        {
          "id": "M-16",
          "dups": 2,
          "payoutPerDup": "$1,052.69"
        }
      ],
      "fraction": 0.03018621902476367,
      "payout": "$1,282.91"
    },
    {
      "handle": "xiaoming90",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
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
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-02",
          "dups": 5,
          "payoutPerDup": "$306.96"
        },
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-06",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.025914983277263,
      "payout": "$1,101.39"
    },
    {
      "handle": "Metatron",
      "ids": [
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
        },
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.024669587882341186,
      "payout": "$1,048.46"
    },
    {
      "handle": "0xsanson",
      "ids": [
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        },
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
        }
      ],
      "fraction": 0.02138179845815724,
      "payout": "$908.73"
    },
    {
      "handle": "Kenshin",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.019604509793438057,
      "payout": "$833.19"
    },
    {
      "handle": "cccz",
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
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-07",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.0184858506958163,
      "payout": "$785.65"
    },
    {
      "handle": "0xNineDec",
      "ids": [
        {
          "id": "M-02",
          "dups": 5,
          "payoutPerDup": "$306.96"
        },
        {
          "id": "M-03",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.01845004279567658,
      "payout": "$784.13"
    },
    {
      "handle": "danb",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.018132012251829213,
      "payout": "$770.61"
    },
    {
      "handle": "PwnedNoMore",
      "ids": [
        {
          "id": "H-03",
          "dups": 6,
          "payoutPerDup": "$767.41"
        }
      ],
      "fraction": 0.018056743799994023,
      "payout": "$767.41"
    },
    {
      "handle": "auditor0517",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        }
      ],
      "fraction": 0.016637429772155425,
      "payout": "$707.09"
    },
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
    },
    {
      "handle": "reassor",
      "ids": [
        {
          "id": "M-08",
          "dups": 3,
          "payoutPerDup": "$631.61"
        }
      ],
      "fraction": 0.014861517530859278,
      "payout": "$631.61"
    },
    {
      "handle": "0x52",
      "ids": [
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        }
      ],
      "fraction": 0.013929488074281104,
      "payout": "$592.00"
    },
    {
      "handle": "zishansami",
      "ids": [
        {
          "id": "H-01",
          "dups": 7,
          "payoutPerDup": "$592.00"
        }
      ],
      "fraction": 0.013929488074281104,
      "payout": "$592.00"
    },
    {
      "handle": "0xc0ffEE",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-09",
          "dups": 4,
          "payoutPerDup": "$426.34"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        }
      ],
      "fraction": 0.010946259086694174,
      "payout": "$465.22"
    },
    {
      "handle": "pedroais",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-09",
          "dups": 4,
          "payoutPerDup": "$426.34"
        }
      ],
      "fraction": 0.01073982402524508,
      "payout": "$456.44"
    },
    {
      "handle": "sashik_eth",
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
          "id": "M-02",
          "dups": 5,
          "payoutPerDup": "$306.96"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        }
      ],
      "fraction": 0.010638938909786996,
      "payout": "$452.15"
    },
    {
      "handle": "exd0tpy",
      "ids": [
        {
          "id": "M-03",
          "dups": 4,
          "payoutPerDup": "$426.34"
        }
      ],
      "fraction": 0.010031524333330013,
      "payout": "$426.34"
    },
    {
      "handle": "Treasure-Seeker",
      "ids": [
        {
          "id": "M-15",
          "dups": 4,
          "payoutPerDup": "$426.34"
        }
      ],
      "fraction": 0.010031524333330013,
      "payout": "$426.34"
    },
    {
      "handle": "shenwilly",
      "ids": [
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        },
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        }
      ],
      "fraction": 0.005604604876859791,
      "payout": "$238.20"
    },
    {
      "handle": "swit",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-04",
          "dups": 6,
          "payoutPerDup": "$230.22"
        }
      ],
      "fraction": 0.005492291591833398,
      "payout": "$233.42"
    },
    {
      "handle": "TrungOre",
      "ids": [
        {
          "id": "M-12",
          "dups": 9,
          "payoutPerDup": "$111.89"
        }
      ],
      "fraction": 0.0026326732460391286,
      "payout": "$111.89"
    },
    {
      "handle": "BowTiedWardens",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.00218582414754831,
      "payout": "$92.90"
    },
    {
      "handle": "ACai",
      "ids": [
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        }
      ],
      "fraction": 0.0021324653292916942,
      "payout": "$90.63"
    },
    {
      "handle": "codexploder",
      "ids": [
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        }
      ],
      "fraction": 0.0021324653292916942,
      "payout": "$90.63"
    },
    {
      "handle": "Critical",
      "ids": [
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        }
      ],
      "fraction": 0.0021324653292916942,
      "payout": "$90.63"
    },
    {
      "handle": "ignacio",
      "ids": [
        {
          "id": "M-13",
          "dups": 10,
          "payoutPerDup": "$90.63"
        }
      ],
      "fraction": 0.0021324653292916942,
      "payout": "$90.63"
    },
    {
      "handle": "Picodes",
      "ids": [
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.0020352872438779263,
      "payout": "$86.50"
    },
    {
      "handle": "GalloDaSballo",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        },
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.0019041206342640252,
      "payout": "$80.93"
    },
    {
      "handle": "dirk_y",
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
        }
      ],
      "fraction": 0.00127108939418415,
      "payout": "$54.02"
    },
    {
      "handle": "antonttc",
      "ids": [
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.001195820942348958,
      "payout": "$50.82"
    },
    {
      "handle": "catchup",
      "ids": [
        {
          "id": "M-11",
          "dups": 13,
          "payoutPerDup": "$50.82"
        }
      ],
      "fraction": 0.001195820942348958,
      "payout": "$50.82"
    },
    {
      "handle": "joestakey",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        }
      ],
      "fraction": 0.0009147347533641604,
      "payout": "$38.88"
    },
    {
      "handle": "defsec",
      "ids": [
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        }
      ],
      "fraction": 0.0008394663015289684,
      "payout": "$35.68"
    },
    {
      "handle": "Sm4rty",
      "ids": [
        {
          "id": "M-10",
          "dups": 15,
          "payoutPerDup": "$35.68"
        }
      ],
      "fraction": 0.0008394663015289684,
      "payout": "$35.68"
    },
    {
      "handle": "0xA5DF",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        }
      ],
      "fraction": 0.0007082996919150672,
      "payout": "$30.10"
    },
    {
      "handle": "chatch",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        }
      ],
      "fraction": 0.0007082996919150672,
      "payout": "$30.10"
    },
    {
      "handle": "itsmeSTYJ",
      "ids": [
        {
          "id": "M-01",
          "dups": 16,
          "payoutPerDup": "$30.10"
        }
      ],
      "fraction": 0.0007082996919150672,
      "payout": "$30.10"
    },
    {
      "handle": "oyc_109",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        },
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 0.00022580535550557578,
      "payout": "$9.60"
    },
    {
      "handle": "0x29A",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "0xDjango",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "AmitN",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "dipp",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "peritoflores",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "rfa",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "simon135",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    },
    {
      "handle": "StErMi",
      "ids": [
        {
          "id": "M-05",
          "dups": 31,
          "payoutPerDup": "$3.20"
        }
      ],
      "fraction": 7.526845183519193e-05,
      "payout": "$3.20"
    }
  ],
  "note": "This tool only calculates shares for Highs and Mediums and will overestimate a little. It does not take into account QA reports."
}
```

## Filter by warden
```
$ ./c4-review test-data/putty.csv 42500 -w sseefried
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

