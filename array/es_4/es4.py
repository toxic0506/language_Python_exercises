#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Si legga da riga di comando una stringa e la si mostri in output
#invertita. Per fare l'inversione si implementi la funzione inverti.

def inverti(s):
    return s[len(s)::-1]

s = input('Inserire una stringa: ')
print(inverti(s))
