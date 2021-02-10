import time, sys
from mfrc522 import SimpleMFRC522

# from time import sleep
# import sys
# from mfrc522 import SimpleMFRC522
# reader = SimpleMFRC522()
#
# try:
#     while True:
#         print("Hold a tag near the reader")
#         id, text = reader.read()
#         print("ID: %s\nText: %s" % (id,text))
#         sleep(5)
# except KeyboardInterrupt:
#     GPIO.cleanup()
#     raise


class RFIDReader():
    def __init__(self):
        self.reader = SimpleMFRC522()
        self.currentText = ""
        while True:
            id, text = self.reader.read()
            print("ID: %s\nText: %s" % (id, text))
            if self.currentText is not text:
                self.currentText = text
                yield self.currentText
            time.sleep(1)
