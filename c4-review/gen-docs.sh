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
	$1
	echo "\`\`\`"
}


echo "## Usage"
echo
fmtCmd "./c4-review --help"
echo
echo "## Without payouts"
echo
fmtCmd "./c4-review test-data/putty.csv"
echo
echo "## With payouts"
echo
fmtCmd "./c4-review test-data/putty.csv 42500"
echo
echo "## Filter by warden"
fmtCmd "./c4-review test-data/putty.csv 42500 -w sseefried"
echo
