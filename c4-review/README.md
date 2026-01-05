# `c4-review`

## Show your appreciation

If you like this tool please let me know [here](https://github.com/code-423n4/backstage-tools/issues/1) by giving me a reaction 👍 👎 ❤️ 👀 🚀.


## Introduction

With `c4-review` you can:
- see a summary of the findings with duplicate counts and a list of handles that found each issue
- estimate your contest payout given the current status of the GitHub finding repo.

Just find the contest/audit slug (e.g. `2025-09-monad`) and try out one of the commands below.

For even prettier output just pipe the command into the `jq` tool.

e.g.

```
$ ./c4-review payouts 2025-09-monad 480000 | jq
```

----

## Installation
`c4-review` is an executable script you can run as a shell command. 

Before running it, you'll need to:
- install Python 3 if you haven't already
- login to the [C4 website](https://code4rena.com/)
- Copy the `C4AUTH-LOGIN` cookie and set it to the `C4AUTH_LOGIN` environment variable:
  - you can use the [EditThisCookie](https://chromewebstore.google.com/detail/editthiscookie-v3/ojfebgpkimhlhcblbalbfjblapadhbol) Chrome extension to read it
  - then you can set it i.e. `export C4AUTH_LOGIN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb2RlNHJlbmEiLCJzdWIiOiI2Z05jd3FZbk1oTSIsImlhdCI6MTczODUxNDEzOCwic2NvcGUiOiJyZWZyZXNoIn0.ABCDEFGHIJKLMNOPQRSTUVWXYZ`


## Usage

### Commands

```
$ ./c4-review --help
```

```
usage: c4-review [-h] {payouts,open} ...

Analyzes the C4 findings data and provides stats. Estimates payout if you provide a handle

positional arguments:
  {payouts,open}

options:
  -h, --help          show this help message and exit
```

### `payouts` command

```
$ ./c4-review payouts --help
```

```
usage: c4-review payouts [-h] [-w [HANDLE]] contest_slug [pot_size]

Find out the fraction of total pot or payouts

positional arguments:
  contest_slug
  pot_size

options:
  -h, --help            show this help message and exit
  -w [HANDLE], --handle [HANDLE]
```

### `open` command

```
$ ./c4-review open --help
```
```
usage: c4-review open [-h] contest_slug handle

Opens all findings from a given warden in browser

positional arguments:
  contest_slug
  handle

options:
  -h, --help    show this help message and exit
```
