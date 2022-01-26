#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#scrivere in C un programma che concatena in un unica stringa le stringhe
#chieste in input da riga di comando.

import sys

s = ""

for i in range(len(sys.argv)-1):
    s += sys.argv[i+1] + " "

print(s)
