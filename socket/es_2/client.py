import socket
import sys
import os


if len(sys.argv)<3 or not os.path.exists(sys.argv[1]):
    print("Errore negli argomenti <file> <porta>")
    exit()
HOST = ""    
PORT = int(sys.argv[2])             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
file = open (sys.argv[1], 'r')
text = file.read()
s.send(text.encode())
str_reverse = s.recv(1024).decode()
print ('Stringa reverse ricevuta dal server: ', str_reverse)
file.close()
s.close()