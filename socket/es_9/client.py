import os, socket, stat, sys

# Verifica dei dati immessi
if len(sys.argv) != 4:
    print "Usare: %s porta ip file" % (sys.argv[0])
    sys.exit(1)
porta = sys.argv[1]
hostname = sys.argv[2]
filename = sys.argv[3]


fd = os.open(filename, os.O_RDONLY)
filesize = os.fstat(fd)[stat.ST_SIZE]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,int(porta)))


while 1:
    buf = os.read(fd, 4096)
    if not buf: break
    s.send(buf)
os.close(fd)
s.close()


print "\nTrasferimento effettuato." 