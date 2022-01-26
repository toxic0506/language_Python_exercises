#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Scrivi un programma che legge da argv[1] un numero intero positivo (N) e poi
#disegna a terminale un quadrato vuoto composto di asterischi (‘*’)
#con il lato lungo N:
#
#Per N pari a 3 il programma stampa:
#
#***
#* *
#***
#Per N pari a 5 il programma stampa:
#
#*****
#*   *
#*   *
#*   *
#*****

import sys

n = int(sys.argv[1])

if(n <= 0):
    exit()

if(n != 1):
    for i in range(n):
        print('*', end="")
    print('')

for i in range(n-2):
    print('*', end="")
    for s in range(n-2):
        print(' ', end="")
    print('*')

for i in range(n):
    print('*', end="")

                

