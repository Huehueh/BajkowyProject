from storytelling.config import ConfigReader
from storytelling.player import AudioPlayer
from storytelling.rfid import RFIDReader
from pymitter import EventEmitter
import signal
import sys

if __name__ == '__main__':
    config = ConfigReader('config.json')
    player = AudioPlayer()
    ee = EventEmitter()
    rfidReader = RFIDReader()
    rfidReader.start_reading(ee)
    signal.signal(signal.SIGINT, exit)

def exit(sig, frame):
    print("Ctrl+C captured, ending read.")
    sys.exit()

@ee.on("start")
def start(id : str):
    print("Start called", id)
    audio_filename = config.get_song_for_id_full_path(id)
    if audio_filename is not None:
        player.play(audio_filename)


@ee.on("pause")
def pause():
    print("Pause called")
    player.pause()
