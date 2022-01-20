ar = []
n = 0
while n < 10:
    ar.append(raw_input('Inserisci un numero: '))
    n = n+1

for num in ar:
    if int(num) % 2 == 0:
        print(num)

for num in ar:
    if int(num) % 2 != 0:
        print(num)
