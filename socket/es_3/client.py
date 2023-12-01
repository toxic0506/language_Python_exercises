import socket
import sys
import os


if len(sys.argv)<4 or not os.path.exists(sys.argv[1]):
    print("Errore negli argomenti <file> <carattere> <porta>")
    exit()
HOST = ""    
PORT = int(sys.argv[3])             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
file = open (sys.argv[1], 'r')
text = file.read()
carattere = sys.argv[2]
s.send(text.encode())
s.recv(1024)
s.send(carattere.encode())
frequenza = s.recv(1024).decode()
print ('Il carattere ', carattere, ' compare ', frequenza, ' volte')
file.close()
s.close()