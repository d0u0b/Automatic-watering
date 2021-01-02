from flask import Flask
from flask_apscheduler import APScheduler
import json
import serial
from record import Recoder

port = "/dev/rfcomm0"
ser = serial.Serial(port,9600)
recorder = Recoder("./record.pickle")

class Config(object):
    JOBS= [
        {
            'id':'job1',
            'func':'__main__:receiveArduino',
            'trigger':'cron',
            'second': "*",
        }
    ]

app = Flask(__name__, static_folder="static")


def receiveArduino():
    try:
        if ser.in_waiting:
            line = ser.readline().decode()
            if line:
                recorder.record(json.loads(line))
    except:
        ser.close()
        ser.open()

@app.route("/chart")
def chart():
    return recorder.chart()

@app.route("/record")
def record():
    return recorder.get_last()

@app.route("/last_water")
def last_water():
    return json.dumps({"time": recorder.last_water()})

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == '__main__':
    try:
        app.config.from_object(Config())
        scheduler = APScheduler()
        scheduler.init_app(app)
        scheduler.start()
        app.run(port=8080, host="0.0.0.0")
    except KeyboardInterrupt:
        ser.close()