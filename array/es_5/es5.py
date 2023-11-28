import sys

concatenata = ""
for i in range(len(sys.argv)):
    if i != 0:
        concatenata += sys.argv[i] + " "
print(concatenata)
    