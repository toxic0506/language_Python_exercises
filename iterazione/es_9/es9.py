#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dati due numeri interi e positivi N1 e N2 con N2>N1, generare e
# visualizzare in ordine decrescente i numeri compresi tra N1 e N2.


n1 = int(input("Inserire il primo numero: "))
n2 = int(input("Inserire il secondo numero: "))

if (n2 <= n1):
    exit()

while (n2 != n1-1):
    print(n2)
    n2 -= 1
