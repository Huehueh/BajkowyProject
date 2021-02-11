import time, sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import signal

class RFIDReader():
    def __init__(self):
        self.reader = SimpleMFRC522()
        self.continue_reading = True
        signal.signal(signal.SIGINT, self.end_read)

    def read(self):
        while self.continue_reading:
            id, text = self.reader.read()
            print("ID: %s\nText: %s" % (id, text))
            yield id
            time.sleep(1)

    def end_read(self, signal, frame):
        print("Ctrl+C captured, ending read.")
        self.continue_reading = False
        GPIO.cleanup()

# reader = RFIDReader()
# reader.read()
