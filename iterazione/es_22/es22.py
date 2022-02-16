#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dato un numero N calcolare e visualizzare tutte le coppie di numeri che
# danno per somma il numero stesso.


n = int(input("Inserire un numero: "))

if(n <= 0):
    exit()

for i in range(0, n+1):
    n1 = i
    n2 = n-n1
    print("%d + %d = %d" % (n1, n2, n))
