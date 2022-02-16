#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Dati due numeri interi positivi N1 e N2 con N2>N1, generare e
#visualizzare in ordine crescente i numeri interi compresi
#nell'intervallo chiuso [N1,N2]. 

n1 = int(input("Inserire il primo numero: "))
n2 = int(input("Inserire il secondo numero: "))

if (n2 < n1):
    exit()

for i in range(n1, n2):
    print(i, end=" ")
    i += 1
print()