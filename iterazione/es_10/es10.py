#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dato N un numero intero positivo, calcolare e visualizzare la somma dei
# primi N numeri interi.


somma = 0
n = int(input("Inserire un numero: "))

if (n <= 0):
    exit()

for i in range(1, n):
    somma += i

print("La somma dei primi %d valori é: %d" % (n, somma))
