#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che effettui la lettura da tastiera di una serie
#di coppie di valori numerici reali (sia positivi che negativi che zero).
#Per ciascuna coppia, l’algoritmo deve calcolare e stampare il valore
#della radice quadrata del rapporto tra il valore maggiore e quello
#minore dei due. Il programma termina quando vengono inseriti dei valori
#che non permettono di svolgere il calcolo nel dominio dei numeri reali.
#Prima di terminare si richiede di stampare un messaggio che indichi la
#ragione per cui non è stato possibile svolgere il calcolo.

import math

while True:
    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("Inserisci il secondo numero: "))

    if n1 <= n2:
        rapporto = n2 / n1
    else:
        rapporto = n1 / n2

    if rapporto >= 0:
        radice = math.sqrt(rapporto)
        print(radice)
    else:
        print("Il rapporto tra i due valori inseriti minore di 0: impossibile fare la radice quadrata")
        break

