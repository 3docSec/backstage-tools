#!/bin/bash

#
# Automatically generates examples that you can copy-paste into
# README.md
#

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $THIS_DIR

function fmtCmd() {
    echo "\`\`\`"
	echo "\$ $1"
    echo "\`\`\`"
    echo
if [ "$2" = "" ]; then
       echo "\`\`\`"
else
       echo "\`\`\`json"
fi
    LINES=$($1 | wc -l)
    if [ "$LINES" -gt 100 ]; then
	  $1 | head -100
	  echo "\"... continued ...\""
	else
	  $1
    fi
	echo "\`\`\`"
}


echo "## Usage"
echo
fmtCmd "./c4-review --help"
echo
echo "## Without payouts"
echo
fmtCmd "./c4-review test-data/putty.csv" yes
echo
echo "## With payouts"
echo
fmtCmd "./c4-review test-data/putty.csv 42500" yes
echo
echo "## Filter by warden"
fmtCmd "./c4-review test-data/putty.csv 42500 -w sseefried" yes
echo
