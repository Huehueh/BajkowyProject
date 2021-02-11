from config import ConfigReader
from player import AudioPlayer
from rfid import RFIDReader

if __name__ == '__main__':
    config = ConfigReader('config.json')
    player = AudioPlayer()
    rfidReader = RFIDReader()

    for id in rfidReader.read():
        print("ID", id)
        audio_filename = config.load(id)
        if audio_filename is not None:
            print(audio_filename)
            player.play(audio_filename)


