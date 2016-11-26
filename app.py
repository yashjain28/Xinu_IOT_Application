import socket
from flask import Flask, request
app = Flask(__name__)

UDP_IP = "192.168.1.3"
UDP_PORT = 22
MESSAGE = "sum 123 4567"

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.settimeout(5.0)

@app.route("/")
def slash():

    resp = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print resp
    #data, address = sock.recvfrom(UDP_PORT)
    return "80"

@app.route("/index")
def home():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()