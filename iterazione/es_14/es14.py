#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dati due numeri interi positivi N1 ed N2 calcolare, mediante la somma
# ripetuta, il prodotto dei due numeri e visualizzarli.


prodotto = 0
n1 = int(input("Inserire il primo numero: "))
n2 = int(input("Inserire il secondo numero: "))

if (n1 < 0 or n2 < 0):
    exit()

for i in range(n2):
    prodotto += n1

print("%d x %d = %d" % (n1, n2, prodotto))
