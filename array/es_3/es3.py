#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Chiedere in input 10 interi e inserirli in un array.
#Stampare a video prima tutti i numeri pari e 
#in seguito tutti i numeri dispari

ar = []
n = 0
while n < 10:
    ar.append(input('Inserisci un numero: '))
    n = n+1

for num in ar:
    if int(num) % 2 == 0:
        print(num)

for num in ar:
    if int(num) % 2 != 0:
        print(num)
