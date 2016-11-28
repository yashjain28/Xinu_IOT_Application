__author__ = 'hemalatha_ganireddy'

import socket

UDP_IP = "192.168.2.4"
UDP_PORT = 22
MESSAGE = "motor FORWARD"

sock_udp = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
resp = sock_udp.sendto(str(len(MESSAGE))+' '+MESSAGE, (UDP_IP, UDP_PORT))
print resp
data, address = sock_udp.recvfrom(22)
print data