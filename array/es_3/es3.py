numeri = []
for i in range(10):
    numeri.append(int(input("Inserisci un numero:")))
pari = []
dispari = []
for num in numeri:
    if num%2 == 0:
        pari.append(num)
    else:
        dispari.append(num)
print(pari)
print(dispari)