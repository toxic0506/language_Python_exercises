import sys

def palindroma(controllo):
    for i in range(int(len(controllo) / 2)):
        if controllo[i] != controllo[len(controllo)-1-i]:
            return False
    return True

if palindroma(sys.argv[1]):
    print(sys.argv[1] + " è palindroma")
else:
    print(sys.argv[1] + " non è palindroma")