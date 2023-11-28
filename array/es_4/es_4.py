import sys


def inverti(stringa):
    i = len(stringa) - 1
    str_reverse = ""
    while i >= 0:
        str_reverse = str_reverse + stringa[i]
        i = i - 1
    return str_reverse


print(inverti(sys.argv[1]))
