#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import time

# input comes from STDIN (standard input)
terms=''
for line in sys.stdin:
    # Limpiamos espacions, buscamos el tabulador y separamos en 2 elementos (tupla)
    if (not re.search('^#',line)):
        # print 'orig: '+line
        line=re.sub('\[.*?]','',line)
        line=re.sub('\(.*?\)','',line)
        terms = line.strip().split('\t')
        if len(terms)>1:
            terms[1]=terms[1].lower()
        # Volcamos la salida por consola
        print '\t'.join(terms)
