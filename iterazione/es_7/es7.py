#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dato N un numero intero positivo maggiore di 1, generare e visualizzare
#il numero precedente. 

n = int(input("Inserire un numero: "))

if (n < 1):
    exit()

print("Il precedente è: %d" %(n-1))