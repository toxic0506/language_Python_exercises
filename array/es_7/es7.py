#!/usr/bin/env pythonprint
# -*- coding: utf-8 -*- 

#Scrivere un programma in che dato un array di interi presi in input mostri
#in output se l'array ha dimensione pari o dispari quando viene inserito 0.

ar = []

while True:
    n = int(input("Inserisci un numero > 0 (termina la serie con 0): "))
    
    if(n == 0):
        if(len(ar) % 2 == 0):
            print("Pari")
        else:
            print("Dispari")
        break

    if(n > 0):
        ar.append(n)
    else:
        break

    
