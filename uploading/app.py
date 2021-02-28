from flask import Flask, request, redirect, url_for, send_from_directory
from storytelling.rfid import RFIDReader
from storytelling.config import ConfigReader
import os

app = Flask(__name__)
configReader = ConfigReader()
app.config['UPLOAD_FOLDER'] = configReader.get_sound_directory()
app.config['UPLOAD_EXTENSIONS'] = ['.mp3']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['MAX_CONTENT_PATH'] = 100000000
reader = None

def init_rfid_reader():
    global reader
    if reader is None or not reader.open:
        reader = RFIDReader()

@app.route("/read_rfid", methods=['GET'])
def read_rfid():
    init_rfid_reader()
    return reader.read_id()

@app.route('/upload_file', methods=['POST'])
def upload_sound():
    uploaded_file = request.files['file']

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
    print("Zapisuje plik", filepath)
    uploaded_file.save(filepath)

    id = request.form["rfid_response"]
    print(f"Zapisuje config {id} - {uploaded_file.filename}")
    configReader.add_song(id, uploaded_file.filename)
    return f"Wrzucono {id} {uploaded_file.filename}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')