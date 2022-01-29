#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dato N un numero intero positivo, generare e visualizzare in ordine crescente i primi N numeri
#interi positivi.

n = int(input("Inserire un numero: "))
for i in range(n):
    print(i+1, end=" ")
print()