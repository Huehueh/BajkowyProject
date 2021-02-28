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
id = None

def init_rfid_reader():
    global reader
    if reader is None or not reader.open:
        reader = RFIDReader()

@app.route("/read_rfid", methods=['GET'])
def rfid():
    global id
    init_rfid_reader()
    id = reader.read_id()
    return id

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_sound():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        print("upload folder", app.config['UPLOAD_FOLDER'])
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        print("Zapisuje plik", filepath)
        uploaded_file.save(filepath)
    return f"wrzucono {uploaded_file.filename}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')