import socket
from flask import Flask, render_template
app = Flask(__name__)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

dev1 = '1'
dev2 = '2'

def send(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(msg)
    data = s.recv(BUFFER_SIZE)
    s.close()
    return data

@app.route("/temp")
def slash():
    MESSAGE = dev2 + "tmpsensor read"
    tempeprature = send(MESSAGE)
    print tempeprature

    tempeprature = float(tempeprature.strip('\0'))/100
    return str(tempeprature)

@app.route("/led1")
def led1():
    MESSAGE = dev2 + "led ON"
    return send(MESSAGE)

@app.route("/led2")
def led2():
    MESSAGE = dev2 + "led OFF"
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
    message=dev1 + 'motor '+var.upper()
    return send(message)

@app.route("/ledvoice")
def led_voice():
    return render_template('ledvoice.html')

@app.route("/buzzer")
def buz_read():
    msg = dev2 + 'buz read'
    return send(msg)

@app.route("/buzz")
def buz_write():
    msg = dev2 + 'buz write'
    return send(msg)

@app.route("/led")
def basic():
    MESSAGE = dev2 +'led read'
    return send(MESSAGE)

@app.route("/motor1")
def motor1():
    msg = dev1 + 'motor read'
    status = int(send(msg))
    print status
    if(status&1==1 or status&2==1):
        return '1'
    return '0'

@app.route("/motor2")
def motor2():
    msg = dev1 + 'motor read'
    status = int(send(msg))
    print status
    if(status&4==1 or status&8==1):
        return '1'
    return '0'

if __name__ == "__main__":
    app.run(host='0.0.0.0')