#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dato N un numero intero positivo, generare e visualizzare in ordine crescente i numeri dispari
#minori o uguali a N.

n = int(input("Inserire un numero: "))
for i in range(n):
    if((i+1) % 2 != 0):
        print(i+1, end=" ")
print()