#!/usr/bin/env python
# -*- coding: utf-8 -*- 


#Si scriva un programma che calcoli l’elevazione a potenza del valore intero
#passato come primo argomento per il secondo argomento intero.

import sys

n = int(sys.argv[1])
e = int(sys.argv[2])

if(n <= 0):
    exit()

print(n**e)
                

