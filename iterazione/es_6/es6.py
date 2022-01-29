#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dato N un numero intero positivo, generare e visualizzare in ordine
#crescente i numeri compresi maggiori uguali di -N e minori uguali di N.

n = int(input("Inserire un numero: "))

menoN = -n

while menoN <= n:
    print(menoN, end=" ")
    menoN += 1

print()
