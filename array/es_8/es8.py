#!/usr/bin/env pythonprint
# -*- coding: utf-8 -*- 


#Progettare un algoritmo che effettui la lettura da tastiera di una serie di valori numerici. Il
#programma termina quando il dato immesso è pari a zero. Calcolare e stampare la media dei valori
#inseriri. Inoltre, stampare la sequenza di valori in ordine inverso rispetto a quello di inserimento. Un
#valore dovrà essere stampato soltanto se maggiore della media calcolata.

ar = []
somma = 0
inseriti = 0

while True:
    n = int(input("Inserisci un numero (termina la serie con 0): "))
    
    if(n == 0):
        media = somma / inseriti
        print("Media = %d" %media)
        v = ar[::-1]
        print("Valori invertiti maggiori della media: ", end="")
        for i in range(len(v)):
            if(v[i] > media):
                print(v[i], end=" ")
        print()

    if(n > 0):
        ar.append(n)
        inseriti += 1
        somma += n
    else:
        break

    
