from flask import Flask, render_template
from rfid import RFIDReader

app = Flask(__name__)
reader = None

def init_rfid_reader():
    global reader
    if reader is None or not reader.open:
        reader = RFIDReader()

@app.route("/read_rfid", methods=['GET'])
def rfid():
    init_rfid_reader()
    return reader.read_id()

if __name__ == "__main__":
    app.run(host='0.0.0.0')