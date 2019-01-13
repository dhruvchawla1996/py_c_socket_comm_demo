import socket

s = socket.socket()
print "Socket successfully created"

port = 3000

s.bind(('', port))
print "Socket binded to %s" %(port)

s.listen(5)
print "Socket is listening"

while True:
    c, addr = s.accept()
    print "Got connection from ", addr

    c.send("Hello! This is server")

    c.close()

