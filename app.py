from flask import Flask
import time

app = Flask(__name__)

def seconds_since_epoch():
    epoch = time.time()
    return int(epoch)

@app.route("/")
def seconds():
    return str(seconds_since_epoch())  # Convert the integer to a string

@app.route("/hours")
def hours():
    seconds = seconds_since_epoch()
    hours = seconds // 3600
    return str(hours)

@app.route("/minutes")
def minutes():
    seconds = seconds_since_epoch()
    minutes = seconds // 60
    return str(minutes)

#and this route returns weeks since epoch
@app.route("/weeks")
def weeks():
    seconds = seconds_since_epoch()
    weeks = seconds // (3600 * 24 * 7)
    return str(weeks)