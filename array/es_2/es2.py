#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Chiedere in input 5 interi e inserirli in un array.
#Stampare a video l'array al contrario.

ar = []
n = 0
while n < 5:
    x = input('Inserisci il numero: ')
    ar.append(x)
    n = n+1
print(ar[::-1])
