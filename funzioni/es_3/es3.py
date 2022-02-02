#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Si crei un programma che nel momento dell'esecuzione popoli l'array
# argv[] con una serie di numeri. Esempio: $ ./a.out 1 5 9 6
# Il programma deve quindi chiedere in input un numero e deve cercarlo
# all'interno dell'array argv.
# Se il numero è presente il programma deve dare un messaggio positivo
# e deve mostrare la posizione dell'elemento, altrimenti deve stampare a
#video: "numero non presente"
# Suggerimento: si usi una funzione per ricercare la posizione dell'
# elemento. Tale funzione deve tornare la posizione oppure -1.


import sys


def ricerca(arr, ric):
    pos = -1
    for i in range(1, len(arr)):
        if(int(arr[i]) == ric):
            pos = i
    return pos


ar = sys.argv
ricercato = int(input("Inserire un numero: "))

res = ricerca(ar, ricercato)

if(res != -1):
    print("Il numero %d é presente nell'array in posizione %d" % (ricercato, res))
else:
    print("Il numero %d non é presente nell'array" % ricercato)
