#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Si scriva un programma in linguaggio C che implementi una funzione
#denominata palindroma che prenda in input una stringa e restituisca
#1 se la stringa è palindroma altrimenti -1

import sys

def palindroma(s):
    t = s[len(s)::-1]
    if (t == s):
        return 1
    else:
        return -1

s = sys.argv[1]
print(palindroma(s))
