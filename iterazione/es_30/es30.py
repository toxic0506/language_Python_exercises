#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dati due numeri interi positivi N1 e N2, verificare se N1 è il quadrato
# di N2.

import math


n1 = int(input("Inserire il primo numero: "))
n2 = int(input("Inserire il secondo numero: "))

if(n1 <= 0 or n2 <= 0):
    exit()

if(math.sqrt(n1) == n2):
    print("%d é il quadrato di %d" % (n1, n2))
else:
    print("%d non é il quadrato di %d" % (n1, n2))
