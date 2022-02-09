
import os, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 50000))
s.listen(1)
conn, addr = s.accept()


fd = os.open("f2.jpg", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0600)

buf=conn.recv(4096)
os.write(fd,buf)

while len (buf)>0:
   
    
    buf = conn.recv(4096)
    os.write(fd,buf)

    
os.close(fd)

conn.close()
