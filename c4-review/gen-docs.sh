#!/bin/bash

#
# Automatically generates examples that you can copy-paste into
# README.md
#

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $THIS_DIR

MAX_LINES=150

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

    FILE=$(mktemp output.XXXXX)
    $1 > $FILE
    LINES=$(cat "$FILE" | wc -l)
    if [ "$LINES" -gt $MAX_LINES ]; then
	  cat $FILE | head -n "$MAX_LINES"
	  echo "\"... continued ...\""
	else
	  cat $FILE
    fi
	echo "\`\`\`"
	rm -f $FILE
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
