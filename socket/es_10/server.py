#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 50000))
s.listen(10)

while 1:
    conn, addr = s.accept()

    filename = conn.recv(4096)
    print("ricezione di %s"%filename.decode())
    conn.send(str(os.path.isfile("./"+filename)).encode())
    print(str(os.path.isfile("./"+filename)))
    if(os.path.isfile("./"+filename)): 
        conn.close()
        continue

    fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0777)

    while 1:
    
        buf = conn.recv(4096)
        if not buf: break
        os.write(fd,buf)
    
    conn.close()

    
os.close(fd)
conn.close()
