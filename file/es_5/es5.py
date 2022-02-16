#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Si scriva un programma che ricerchi un carattere o una stringa dentro ad un file di testo. Al termine della ricerca il programma deve scrivere in un altro file di testo il risultato della ricerca.
#
#Esempio di invocazione:
#$ ./prg.out input.txt output.txt -c p
#$ ./prg.out input.txt output.txt -p ciao
#
#Se in argv[3] compare -c allora si ricercheranno le singole occorrenze del carattere, altrimenti se compare -p si ricercheranno le occorrenze dell’intera stringa.
#
#Esempio di output.txt
#Il carattere p compare 3 volte nel file input.txt
#
#Altro esempio di output.txt
#La stringa ciao compare 5 volte nel file input.txt
#
#Altro esempio di output.txt
#La ricerca non ha prodotto risultati

import sys
import array

class mioArray(array):
    def First(self):
        return self[0]

def leggi(nome):
    f = open(nome, "r")
    x = f.read()
    f.close()
    return x

def ricerca(r, str):
    if(r not in str):
        return -1
    pos = 0
    for i in range(len(str)):
        if(ricercato == str[i]):
            pos += 1
    return pos

def scrivi(res, out):
    f = open(out, "w")
    f.write(res)
    f.close()


if(len(sys.argv) > 1):
    nomeInput = sys.argv[1]
    nomeOut = sys.argv[2]
    parametro = sys.argv[3]
    ricercato = sys.argv[4]
    if(parametro != "-c" and parametro != "-p"):
        print("Il parametro inserito non è corretto!")
        exit()
else:
    print("Valori inseriti non corretti!")
    exit()

str = leggi(nomeInput)
cnt = ricerca(ricercato, str)
res = "La ricerca non ha prodotto risultati"
if(cnt != 0):
    if(parametro == "-p"):
        res = "La stringa %s compare %d volte nel file %s" %(ricercato, cnt, nomeInput)
    else:
        res = "Il carattere %s compare %d volte nel file %s" %(ricercato, cnt, nomeInput)

scrivi(res, nomeOut)



