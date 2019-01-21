#!/usr/bin/env python
import sys

# the reducer file takes as stdin the stdout of mapper, a list of tuples ("word",1)

# temporary variables curr_word and curr_count are created to perform the word count

curr_word = None
curr_count = 0

for line in sys.stdin:
    # first one gets elements each tuple
    word, count = line.split("\t")
    count = int(count)

    if word == curr_word:
        curr_count += count
    else:
        # show how the coun
        if curr_word:
            print("{0}\t{1}".format(curr_word, curr_count))
        # actualizamos el valor de palabra actual y cuenta actual
        curr_word = word
        curr_count = count
# por ultimo contemplamos el caso de que la ultima palabra se repita
if curr_word == word:
print("{0}\t{1}".format(curr_word, curr_count))
