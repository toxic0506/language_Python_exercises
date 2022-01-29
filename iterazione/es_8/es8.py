#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dato N un numero intero positivo, generare e visualizzare in ordine
# decrescente i primi N numeri interi positivi.

n = int(input("Inserire un numero: "))

if (n <= 0):
    exit()

while (n >= 1):
    print(n)
    n -= 1
