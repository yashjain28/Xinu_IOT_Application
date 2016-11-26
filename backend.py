__author__ = 'hemalatha_ganireddy'

import socket

UDP_IP = "192.168.1.3"
UDP_PORT = 22
MESSAGE = "sum 123 4567"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
resp = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, address = sock.recvfrom(22)
print resp