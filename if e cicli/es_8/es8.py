#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che risolve il seguente problema. Si desidera 
#calcolare la somma delle radici quadrate di N valori numerici inseriti 
#dall’utente. 
#L’algoritmo deve stampare la somma calcolata. L’algoritmo deve terminare
#con un messaggio di errore quando viene inserito un numero che non
#permette di effettuare il calcolo (nel dominio dei numeri reali).

import math


somma = 0
num = int(input("Quanti numeri vuoi inserire? "))
while num > 0:
    x = int(input("Inserisci un numero: "))
    if x >= 0:
        somma += math.sqrt(x)
        num -= 1
    else:
        print("Impossibile fare la radice di un numero negativo\n")
        num = 0

print('Somma risultante = %d' %somma)

