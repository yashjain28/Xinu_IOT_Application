#!/usr/bin/env python

import socket

# socket attributes to communicate with xinu udp server
UDP_IP = "192.168.2.4"
UDP_IP_1 = "192.168.2.5"
UDP_PORT = 22


# socket attributes of this tcp server
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
# start server by listening
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "recieved from client: ",data
    sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
    sock.settimeout(5.0)
    resp = sock.sendto(data, (UDP_IP, UDP_PORT)) # connect to udp server and get data
    d, address = sock.recvfrom(UDP_PORT)
    print "received data:", d
    conn.send(d)  # echo
    conn.close()