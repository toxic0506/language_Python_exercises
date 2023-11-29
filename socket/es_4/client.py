import socket
import sys
import os


if len(sys.argv)<4:
    print("Errore negli argomenti <stringa1> <stringa2> <porta>")
    exit()
HOST = ""    
PORT = int(sys.argv[3])             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
string1 = sys.argv[1]
string2 = sys.argv[2]
s.send(string1.encode())
str_reverse = s.recv(1024).decode()
print ('Stringa 1 reverse ricevuta dal server: ', str_reverse)
s.send(string2.encode())
str_reverse = s.recv(1024).decode()
print ('Stringa 2 reverse ricevuta dal server: ', str_reverse)
s.close()