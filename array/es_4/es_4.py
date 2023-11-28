import sys
def inverti(corretta):
    i=len(corretta) -1
    str_reverse=""
    while i>=0:
        str_reverse = str_reverse+corretta[i]
        i=i-1
    return str_reverse

print(inverti(sys.argv[1]))