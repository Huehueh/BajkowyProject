from flask import Flask, request, redirect, url_for, send_from_directory
from storytelling.rfid import RFIDReader
from storytelling.config import ConfigReader
import os

app = Flask(__name__)
configReader = ConfigReader()
app.config['UPLOAD_FOLDER'] = configReader.get_sound_directory()
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
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
    if 'file' in request.files:
        uploaded_file = request.files['file']
        filename = uploaded_file.filename
        if filename != '':
            id = request.form["rfid_response"]
            validId = configReader.add_song(id, filename)
            if validId:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print("Saving file", filepath)
                uploaded_file.save(filepath)

                return f"Wrzucono {id} {filename}"
    return "Nie wrzucono pliku"


if __name__ == "__main__":
    app.run(host='0.0.0.0')