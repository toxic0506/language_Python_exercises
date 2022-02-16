from hashlib import md5
import os
import socket
import sys

# Verifica dei dati immessi
if (len(sys.argv) != 4):
    print("Usare: %s porta ip file" % sys.argv[0])
    exit(1)

porta = sys.argv[1]
hostname = sys.argv[2]
filename = sys.argv[3]

fd = os.open(filename, os.O_RDONLY)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, int(porta)))

s.send(filename.encode())
file_exists = s.recv(4096).decode()

if(file_exists == "True"):
    print("Nome file già presente")
    exit(1)

stringmd5 = b''

while True:
    buf = os.read(fd, 4096)
    if not buf:
        break
    s.send(buf)
    stringmd5 += md5(buf).digest()
    print(stringmd5)

os.close(fd)

print("Trasferimento effettuato.")

stringRec = b''

while True:
    buf = s.recv(4096)
    if not buf:
        break
    stringRec += md5(buf).digest()
    print(stringRec)

print("Ricevuto md5")

if(stringmd5 == stringRec):
    print("Le due chiavi corrispondono")
else:
    print("Le due chiavi sono diverse")

s.close()
