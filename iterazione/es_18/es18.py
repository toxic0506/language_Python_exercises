#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Data una misura di tempo espressa in secondi S1, convertirla in ore H,
# minuti M e secondi S.
# Descrivere il problema mediante flow chart.
# Esempio: se il numero dei secondi è 1630, si dovrà ottenere, in uscita
# dal programma, 0h 27m 10s.


inp = int(input("Inserire un numero (in secondi): "))

if (inp < 0):
    exit()

ore = 0
minuti = 0
secondi = inp
while(secondi > 60):
    secondi -= 60
    minuti += 1
    if(minuti > 60):
        ore += 1
        minuti -= 60


print("%d secondi = %dh %dm %ds" % (inp, ore, minuti, secondi))
