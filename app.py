import socket
from flask import Flask, render_template
app = Flask(__name__)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


def send(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(msg)
    data = s.recv(BUFFER_SIZE)
    s.close()
    return data

@app.route("/")
def slash():
    MESSAGE = "tmpsensor read"
    return send(MESSAGE)

@app.route("/led1")
def led1():
    MESSAGE = ""
    #sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    #data, address = sock.recvfrom(UDP_PORT)
    return "OK"

@app.route("/led2")
def led2():
    MESSAGE = ""
    return send(MESSAGE)

@app.route("/index")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')