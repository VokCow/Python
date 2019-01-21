#!/usr/bin/env python
import sys

# read lines from stdin

for line in sys.stdin:
    words = line.split()
# stdout is in the form ("word", 1) and it will be input for reducer.py file 
    for word in words:
print("{0}\t{1}".format(word, 1))
