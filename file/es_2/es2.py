#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Chiedere in input l'eta e il nome di 5 persone. Salvarle in un'apposita
# struttura dati. Calcolare il più vecchio e scrivere l'output sia a video
# che in un file di testo chiamato "vecchio.txt".
# Si utilizzi la seguente struttura dati:
#
# typedef struct{
#	char nome[30];
#	int eta;
# }persona;

import string


class Persona:

    nome: string
    eta: int

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta


def anziano(arr):
    pos = 0
    for i in range(len(arr)):
        if(arr[pos].eta < arr[i].eta):
            pos = i
    return pos


def scrivi(nome, s):
    f = open(nome, "w")
    f.write(s)
    f.close()


NUM_PERS = 5
persone = []
for i in range(NUM_PERS):
    n = input("Inserisci il nome: ")
    e = -1
    while (e < 0):
        e = int(input("Inserisci l'etá: "))
    persone.append(Persona(n, e))

pos = anziano(persone)
p = persone[pos]

s = "La persona piú anziana é: %s, %d anni" % (p.nome, p.eta)
print(s)

scrivi("vecchio.txt", s)
