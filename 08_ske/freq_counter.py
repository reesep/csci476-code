#!/usr/bin/python

# quick and dirty python script to count frequencies of
# unigrams, bigrams, and trigrams in a corpus of text.
#
# Usage: ./freq_counter.py < mytextfile

import sys
import csv
import re
from collections import Counter
from itertools import tee, islice

def write_to_csv(filename, data):
    print('writing csv data to: ' + filename)
    x, y = zip(*data)
    x = [ ''.join(_) for _ in x]
    y = list(y)
    data = [x, y]
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("...done!")

def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break

#
# print 1grams (unigrams) & bigrams & trigrams
#

topN = 10
content = None
with sys.stdin as f:
    content = [line.strip() for line in f]
    content = ' '.join(content)        # build 1 big string
    content = content.replace(' ', '') # don't count whitespace

print("\nletter frequencies (all):")
unigrams = Counter(ngrams(list(content), 1))
total = sum(unigrams.values())
for x in unigrams.most_common():
    perc = " ({:.2f}%)".format((x[1]/float(total))*100)
    print( ''.join(x[0]) + ' : ' + str(x[1]) + perc )

write_to_csv('1grams.csv', unigrams.most_common())

print("\ntop %i bigrams:" % topN)
bigrams = Counter(ngrams(list(content), 2))
total = sum(bigrams.values())
for x in bigrams.most_common(topN):
    perc = " ({:.2f}%)".format((x[1]/float(total))*100)
    print( ''.join(x[0]) + ' : ' + str(x[1]) + perc )

write_to_csv('2grams.csv', bigrams.most_common(topN))

print("\ntop %i trigrams:" % topN)
trigrams = Counter(ngrams(list(content), 3))
total = sum(trigrams.values())
for x in trigrams.most_common(topN):
    perc = " ({:.2f}%)".format((x[1]/float(total))*100)
    print( ''.join(x[0]) + ' : ' + str(x[1]) + perc )

write_to_csv('3grams.csv', trigrams.most_common(topN))
