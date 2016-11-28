import socket
from flask import Flask, render_template
app = Flask(__name__)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


def send(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(str(len(msg))+' '+msg)
    data = s.recv(BUFFER_SIZE)
    s.close()
    return data

@app.route("/temp")
def slash():
    MESSAGE = "tmpsensor read"
    tempeprature = send(MESSAGE)
    print tempeprature

    tempeprature = float(tempeprature.strip('\0'))/100
    return str(tempeprature)

@app.route("/led1")
def led1():
    MESSAGE = "led ON"
    return send(MESSAGE)

@app.route("/led2")
def led2():
    MESSAGE = "led OFF"
    return send(MESSAGE)

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/dash")
def h():
    return render_template('dashboard.html')

@app.route("/car")
def car():
    return render_template('car.html')

@app.route("/motor/<var>")
def motor(var):
    message='motor '+var.upper()
    return send(message)

@app.route("/led")
def basic():
    return "ON"

if __name__ == "__main__":
    app.run(host='0.0.0.0')