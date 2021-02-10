from config import ConfigReader
from player import AudioPlayer
from rfid import RFIDReader


if __name__ == '__main__':
    reader = ConfigReader('config.json')
    player = AudioPlayer()
    rfidReader = RFIDReader()

    while True:
        inp = input()
        status, audio_filename = reader.read_config(inp)
        if status == 0:
            print(audio_filename)
            player.play(audio_filename)
        elif inp == "p":
            player.pause()
        elif inp == "q":
            break


