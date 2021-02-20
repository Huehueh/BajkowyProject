from flask import Flask, render_template
from rfid import RFIDReader

app = Flask(__name__)

@app.route("/hue/read_rfid", methods=['GET'])
def rfid():
    reader = RFIDReader()
    return reader.read_rfid()

@app.route("/hue")
def render():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')