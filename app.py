import socket
from flask import Flask, request
app = Flask(__name__)

UDP_IP = "192.168.2.4"
UDP_PORT = 22

# intialize socket object
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.settimeout(5.0)

@app.route("/")
def slash():
    MESSAGE = "tmpsensor read"
    resp = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print resp
    data, address = sock.recvfrom(UDP_PORT)
    return data

@app.route("/led1")
def led1():
    MESSAGE = ""
    #sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    #data, address = sock.recvfrom(UDP_PORT)
    return "OK"

@app.route("/led2")
def led2():
    MESSAGE = ""
    sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    data, address = sock.recvfrom(UDP_PORT)
    return data

@app.route("/index")
def home():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')