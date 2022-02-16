#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Progettare un algoritmo che risolva il seguente problema. Si richieda 
#all’utente di inserire una serie di terne di dati numerici (A, B, C). 
#Il programma deve terminare quando uno dei valori inseriti è minore di
#zero. Si scartino le terne nelle quali i valori non sono in ordine
#strettamente crescente, ovvero quelle terne per cui non valga A < B < C.
#Su tutte le terne non scartate si calcoli il massimo e il minimo dei
#valori inseriti. Si stampino a video tali valori massimi e minimi prima
#di terminare il programma.

import sys

minimo = sys.maxsize
massimo = 0

while True:
    a = int(input("Inserisci il primo numero: "))
    if a > 0:
        b = int(input("Inserisci il secondo numero: "))
        if b > 0:
            if a < b:
                c = int(input("Inserisci il terzo numero: "))
                if c > 0 and a < b < c:
                    if minimo > a:
                        minimo = a
                        print("Minimo = %d" %minimo)
                    if massimo < c:
                        massimo = c
                        print("Massimo = %d" %massimo)              
        else:
            print('Massimo = %d, Minimo = %d' %(massimo, minimo))
            break
    else:
        print('Massimo = %d, Minimo = %d' %(massimo, minimo))
        break
                

