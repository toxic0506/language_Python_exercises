#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che effettui le seguenti operazioni:
#continui a leggere da tastiera una serie di terne di valori interi A ,
#B e C finchè non vengono inseriti dei valori tali per cui A + B < C
#conteggi il numero di volte in cui la differenza tra A e B e pari, dispari, e quando e nulla
#prima di terminare, visualizzi il valore dei valori conteggiati


nPari = 0
nDispari = 0
nNulli = 0

while True:
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    c = float(input("Inserisci il terzo numero: "))

    if (a - b % 2 == 0):
        nPari += 1
    elif (a - b == 0):
        nNulli += 1
    else:
        nDispari += 1

    if (a+b < c):
        print("Differenza pari = %d" %nPari)
        print("Differenza dispari = %d" %nDispari)
        print("Differenza nulla = %d" %nNulli)
        break

