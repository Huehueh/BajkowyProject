from flask import Flask
from rfid import RFIDReader

app = Flask(__name__)

@app.route("/read_rfid")
def rfid():
    reader = RFIDReader()
    return reader.read_rfid()

if __name__ == "__main__":
    app.run(host='0.0.0.0')