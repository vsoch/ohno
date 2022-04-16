#!/bin/bash

echo
echo "************** START: test_client.sh **********************"

# Create temporary testing directory
echo "Creating temporary directory to work in."
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
shpc_root="$( dirname "${here}" )"

. $here/helpers.sh

# Create temporary testing directory
tmpdir=$(mktemp -d)
output=$(mktemp ${tmpdir:-/tmp}/ohno_test.XXXXXX)
printf "Created temporary directory to work in. ${tmpdir}\n"

# Make sure it's installed
if ! command -v ohno &> /dev/null
then
    printf "ohno is not installed\n"
    exit 1
else
    printf "ohno is installed\n"
fi

echo
echo "#### Testing base client "
runTest 0 $output ohno --version

echo
echo "#### Testing monitor "
runTest 0 $output ohno monitor --help
runTest 0 $output ohno monitor python ../../examples/monitor/failure.py

echo
echo "#### Testing parse "
runTest 0 $output ohno parse --help
runTest 0 $output ohno parse ../../examples/parse/spack-error.txt

rm -rf ${tmpdir}
