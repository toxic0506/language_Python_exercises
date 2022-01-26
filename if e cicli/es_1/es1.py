#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che effettui la lettura da tastiera di una serie di coppie di valori numerici.
#L algoritmo deve calcolare e stampare il rapporto tra il valore minore e quello maggiore dei due. Il
#programma termina quando uno dei due valori o entrambi sono uguali a zero.


while True:
    n1 = float(input('Primo numero: '))
    n2 = float(input('Secondo numero: '))

    if n1 <= n2:
        rapporto = n1 / n2
    if n2 <= n1:
        rapporto = n2 / n1
 
    print(rapporto)

    if n2 == 0 or n1 == 0:
        break