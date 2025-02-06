# File Comparators
Given two sorted input files, produces two output files (`a_not_b.txt` and `b_not_a.txt`) representing the disjoint set of elements.
Assumes lines end in `\n`. Assumes files are ASCII. Assumes no empty lines in the files.

## To install
`pipenv install`

## mvp1.py
Assumes files to be compared are local files named a.txt and b.txt.

USAGE:
`pipenv run python mvp1.py

## mvp2.py
USAGE:
`pipenv run python mvp2.py --file1 <filename> --file2 <filename>`

For example:
`pipenv run python mvp2.py --file1 a.txt --file2 b.txt`