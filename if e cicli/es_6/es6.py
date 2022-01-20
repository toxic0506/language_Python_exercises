#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che effettui le seguenti operazioni:
#legga da tastiera una coppia di valori interi A e B con A<B;
#continui a leggere da tastiera una serie di valori interi, terminando 
#quando il valore letto e al di fuori dell intervallo [A, B];
#conteggi la media dei valori letti;
#prima di terminare, stampi il valore calcolato.

somma = 0
letti = 0

a = float(raw_input("Inserisci A: "))
b = float(raw_input("Inserisci B: "))

if a < b:
    while True:
        n = int(raw_input("Inserisci un numero: "))
        letti += 1
        if n > a and n < b:
            somma += n
        else:
            media = somma / letti
            print("Media = {0}", media)
            break

