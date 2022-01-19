#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    n1 = int(raw_input("Inserisci il primo numero: "))
    n2 = int(raw_input("Inserisci il secondo numero: "))

    prodotto = n1 * n2
    #print("prodotto = ", prodotto)
    somma += prodotto
    #print("somma = ", somma)

    if n1 == 0 or n2 == 0:
        print("totale = {0}", somma)
        break

