from flask import Flask, request, redirect, url_for, send_from_directory
from storytelling.rfid import RFIDReader
from storytelling.config import ConfigReader
import os

app = Flask(__name__)
configReader = ConfigReader()
app.config['UPLOAD_FOLDER'] = configReader.get_sound_directory()
app.config['UPLOAD_EXTENSIONS'] = ['.mp3']
app.config['UPLOAD_PATH'] = 'uploads'
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

@app.route('/', methods='POST')
def upload_sound():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print("PliczeK", uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH', uploaded_file.filename))
    return redirect(url_for('index'))
    #

@app.route('/uploads/<filename>')
def upload(filename):
    configReader.add_song(id, filename)
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0')