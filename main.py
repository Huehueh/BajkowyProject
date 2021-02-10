from config import ConfigReader
from player import AudioPlayer
from rfid import RFIDReader

if __name__ == '__main__':
    reader = ConfigReader('config.json')
    player = AudioPlayer()
    rfidReader = RFIDReader()

    while True:
        inp = input()
        audio_filename = reader.read_config(inp)
        if audio_filename is not None:
            print(audio_filename)
            player.play(audio_filename)
        elif inp == "p":
            player.pause()
        elif inp == "q":
            break


