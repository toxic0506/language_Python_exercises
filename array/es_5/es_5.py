import sys

concatenata = ""
for i in range(1, len(sys.argv)):
    concatenata += sys.argv[i] + " "
print(concatenata)
