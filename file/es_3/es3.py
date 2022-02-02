#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere il file studenti.txt e mostrare a video il nome e il cognome
# dello studente piu vecchio e la media dell'eta degli studenti.
# Si usi la seguente struttura dati per memorizzare le informazioni
# dello studente
#
# typedef struct{
#	char nome[20];
#	char cognome[20];
#	int eta;
# }studente_t;


import string


class Persona:

    nome: string
    cognome: string
    eta: int

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta


def leggi(nome):
    f = open(nome, "r")
    return f.read()


def anziano(arr):
    pos = 0
    for i in range(len(arr)):
        if(arr[pos].eta < arr[i].eta):
            pos = i
    return pos


def mediaEta(arr):
    somma = 0
    for i in range(len(arr)):
        somma += int(arr[i].eta)
    return somma / len(arr)


def creaPersone(s):
    ar = []
    s = s.replace("\n", " ")
    s = s.split(" ")
    for i in range(0, len(s)-1, 3):
        nome = s[i]
        cognome = s[i+1]
        eta = s[i+2]
        ar.append(Persona(nome, cognome, eta))
    return ar


persone = leggi("studenti.txt")
persone = creaPersone(persone)

pos = anziano(persone)
media = mediaEta(persone)

vecchio = persone[pos]

print("Il piú anziano é: %s %s, %d anni" %
      (vecchio.nome, vecchio.cognome, int(vecchio.eta)))
print("La media delle etá é: %d" % media)
