#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dato un numero intero positivo N verificare se N è un numero primo.

n = int(input("Inserire un numero: "))

if(n <= 0):
    exit()

primo = True
for i in range(2, n):
    if(n % i == 0):
        primo = False

if(primo):
    print("%d é un numero primo" % n)
else:
    print("%d non é un numero primo" % n)
