def inverti(s):
    index = 0
    last = len(s)-1
    for st in s:
        a = s[last]
        s[last] = st
        s[index] = a
        index += 1
        last -= 1



s = raw_input('Inserire una stringa: ')
inverti(s)
print(s)
