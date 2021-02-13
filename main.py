from config import ConfigReader
from player import AudioPlayer
from rfid import RFIDReader
from pymitter import EventEmitter

ee = EventEmitter()

if __name__ == '__main__':
    config = ConfigReader('config.json')
    player = AudioPlayer()
    rfidReader = RFIDReader(ee)
    rfidReader.start_reading()

@ee.on("start")
def start(id):
    print("Start called", id)
    audio_filename = config.load(str(id))
    if audio_filename is not None:
        print(audio_filename)
        player.play(audio_filename)


@ee.on("pause")
def pause():
    print("Pause called")
    player.pause()
