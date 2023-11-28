arr = []
num = int(input("Inserisci numero: "))
while num!=0:
    arr.append(num)
    num = int(input("Inserisci numero: "))

somma = 0
for i in arr:
    somma+=i

media = somma / len(arr)
print(media)

reverse = arr[::-1]
for i in reverse:
    if i>=media:
        print(i)
