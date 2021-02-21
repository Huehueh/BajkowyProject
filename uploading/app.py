from flask import Flask, request, redirect, url_for
from storytelling.rfid import RFIDReader
from storytelling.config import ConfigReader

ALLOWED_EXTENSIONS = {'mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
configReader = ConfigReader()
app['UPLOAD_FOLDER'] = configReader.get_sound_directory()
reader = None

def init_rfid_reader():
    global reader
    if reader is None or not reader.open:
        reader = RFIDReader()

@app.route("/read_rfid", methods=['GET'])
def rfid():
    init_rfid_reader()
    return reader.read_id()

# @app.post("/upload_sound")
# def upload_sound(sound):
#     try:
#         sound.file.seek(0)

@app.route('/', methods='POST')
def upload_sound():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print("PliczeK", uploaded_file.filename)
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))
    # configReader.add_song(id, soundname)

if __name__ == "__main__":
    app.run(host='0.0.0.0')