import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 50000))
s.listen(10)

while True:
    conn, addr = s.accept()

    filename = conn.recv(4096).decode()

    exist = os.path.isfile("./" + filename)
    conn.send(str(exist).encode())

    if(exist):
        print("Nome file giá presente")
        conn.close()
        continue

    fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o777)

    print("Ricezione di %s" % filename)

    while True:
        buf = conn.recv(4096)
        if not buf:
            break
        os.write(fd, buf)

    print("Ricevuto")
    conn.close()
    os.close(fd)
