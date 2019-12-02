#!/usr/bin/env python
from operator import itemgetter
import sys
import re

current_word = None
word = None
trad_complete = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().split('\t')

    # parse the input we got from mapper.py
    word = line[0]
    try:
       trad = line[1]
    except:
       trad = ''
       pass
    if current_word == word:
#        if not re.search(trad,trad_complete):
        if trad_complete.find(trad)<0:
            trad_complete = trad_complete + "|" + trad
    else:
        if current_word:
            print '%s\t%s' % (current_word, trad_complete)
        trad_complete = trad
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, trad_complete)
