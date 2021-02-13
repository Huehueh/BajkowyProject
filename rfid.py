import time, sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import signal
from threading import Thread, Lock, Event
from pymitter import EventEmitter

timeout=2

class RFIDReader:
    def __init__(self, ee : EventEmitter):
        self.reader = SimpleMFRC522()
        signal.signal(signal.SIGINT, self.end_read)
        self.timeRead = 0
        self.currentId = 0
        self.newId = 0
        self.ee = ee
        self.reading = False


    def start_reading(self):
        self.stop_event = Event()
        self.thread1 = Thread(target=self.read_rfid, args=[self.stop_event])
        self.thread2 = Thread(target=self.check_state, args=[self.stop_event])
        self.thread1.start()
        self.thread2.start()

    def check_state(self, stop_event : Event):
        while not stop_event.is_set():
            currentTime = time.time()
            if currentTime - self.timeRead > timeout and self.reading:
                self.ee.emit("pause")
                self.reading = False
            elif self.newId != self.currentId:
                self.currentId = self.newId
                self.reading = True
                self.ee.emit("start", self.currentId)
            time.sleep(1)

    def read_rfid(self, stop_event : Event):
        while not stop_event.is_set():
            id, text = self.reader.read()
            print("ID: %s\nText: %s" % (id, text))
            self.newId = id
            self.timeRead = time.time()
            time.sleep(1)

    def end_read(self, sig, frame):
        print("Ctrl+C captured, ending read.")
        self.stop_event.set()
        self.thread1.join()
        GPIO.cleanup()
