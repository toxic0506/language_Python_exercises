#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Scrivere un programma in linguaggio Python che legge in input un file di testo che rappresenta una rubrica telefonica.
# La rubrica è composta da nome, cognome, numero di telefono.
#
# Esempio di file testo:
#
# $ cat rubrica.txt
# francesco veronese 3405625874
# marco bisco 3654215847
#
# Attraverso un menu si vogliono poter eseguire le seguenti operazioni:
#
# 1) mostrare la rubrica a video
# 2) aggiungere un contatto alla rubrica
# 3) eliminare un contatto dalla rubrica dopo averlo ricercato con il suo numero di telefono
#
#
# Osservazioni: si strutturi il programma usando le funzioni, si adoperi un’opportuna struct per mappare la rubrica telefonica.
#
# Il programma deve dare l’opportunità all’utente di decidere se sovrascrivere la rubrica con I nuovi dati oppure se scrivere in un nuovo file di testo.
#
#
# Esempi di utilizzo del programma:
#
# 1) $ ./rubrica.out rubrica.txt
# 2) $ ./rubrica.out rubrica.txt -f output.txt
#
# Nel caso 1) il programma sovrascrive il file in argv[1]. Nel caso 2) il programma scrive nel file argv[3]

import string
import sys


class Persona:

    nome: string
    cognome: string
    telefono: string

    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
    
    def __str__(self) -> str:
        return (self.cognome + " " + self.nome + " " + self.telefono)


def leggi(nome):
    f = open(nome, "r")
    x = f.read()
    f.close()
    return x

def formatta(ar):
    vett = []
    for i in range(len(ar)):
        s = ""
        s += ar[i].nome + " "
        s += ar[i].cognome + " "
        s += ar[i].telefono + "\n"
        vett.append(s)
    return vett

def scrivi(ar, out):
    f = open(out, "w")
    for i in range(len(ar)):
        f.write(ar[i])
    f.close()


def creaPersone(s):
    ar = []
    s = s.replace("\n", " ")
    s = s.split(" ")
    for i in range(0, len(s)-1, 3):
        nome = s[i]
        cognome = s[i+1]
        telefono = s[i+2]
        ar.append(Persona(nome, cognome, telefono))
    return ar


def visualizza(pers):
    for i in range(len(pers)):
        p = pers[i]
        print("%s %s, %s" % (p.nome, p.cognome, p.telefono))


def ricerca(persone, numero):
    for i in range(len(persone)):
        if(persone[i].telefono == numero):
            return i
    return -1


def aggiungi(persone, nuova):

    # controllo che non esista un altro contatto con lo stesso numero di telefono
    if(ricerca(persone, nuova.telefono) == -1):
        persone.append(nuova)
        return True
    else:
        return False


def rimuovi(persone, numero):
    pos = ricerca(persone, numero)
    if(pos != -1):
        del persone[pos]
        return True
    else:
        return False


nomeFile = ""
nomeOut = ""
if(len(sys.argv) > 1):  # deve esserci almeno un parametro
    nomeFile = sys.argv[1]
    if(len(sys.argv) == 4):
        if(sys.argv[2] == "-f"):
            parametro = sys.argv[2]
            nomeOut = sys.argv[3]
        else:
            print("Il parametro non è corretto!")
            exit()
    else:
        nomeOut = nomeFile

if(nomeFile == ""):
    print("Numero di parametri non valido!")
    exit()

persone = leggi(nomeFile)
persone = creaPersone(persone)
ar = formatta(persone)
print(ar)

while True:
    print("\n------ MENÚ ------")
    print("1) Visualizza la rubrica")
    print("2) Aggiungi un contatto")
    print("3) Elimina un contatto")

    scelta = int(input("\nScegli un'opzione (1-3): "))

    if (scelta == 1):
        visualizza(persone)
    elif (scelta == 2):
        nome = input("\nInserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        telefono = input("Inserisci il numero di telefono: ")
        nuova = Persona(nome, cognome, telefono)
        if(aggiungi(persone, nuova)):
            print("\nNuovo contatto aggiunto!")
        else:
            print("\nEsiste giá un contatto con questo numero di telefono")
    elif (scelta == 3):
        ric = input(
            "\nInserisci il numero di telefono del contatto da eliminare: ")
        if(rimuovi(persone, ric)):
            print("\nContatto eliminato!")
        else:
            print("\nNon é presente un contatto con questo numero")
    else:
        print("\nScelta non corretta")
    
    ar = formatta(persone)
    scrivi(ar, nomeOut)

