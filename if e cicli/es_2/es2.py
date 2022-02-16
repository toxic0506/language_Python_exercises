#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Progettare un algoritmo che effettui le seguenti operazioni:
#continui a leggere da tastiera due valori numerici, fermandosi quando uno dei due numeri e
#0 (zero)
#per ogni coppia di numeri letti:
#calcoli il prodotto dei due numeri e ne stampi il valore
#sommi il prodotto calcolato ad una variabile che memorizzi la somma di tutti i prodotti
#all uscita del ciclo, stampi il valore della somma

somma = 0

while True:
    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))

    if n1 == 0 or n2 == 0:
        print("Totale = %d" %somma)
        break

    prodotto = n1 * n2
    print("Prodotto = %d" %prodotto)
    somma += prodotto
    #print("somma = ", somma)

    

