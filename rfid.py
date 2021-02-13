import time, sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from threading import Thread, Lock, Event
from pymitter import EventEmitter

timeout=2

class RFIDReader:
    def __init__(self, ee : EventEmitter):
        self.reader = SimpleMFRC522()
        self.timeRead = 0
        self.currentId = 0
        self.newId = 0
        self.ee = ee


    def start_reading(self):
        self.stop_event = Event()
        self.thread1 = Thread(target=self.read_rfid, args=[self.stop_event])
        self.thread2 = Thread(target=self.check_state, args=[self.stop_event])
        self.thread1.start()
        self.thread2.start()


    def check_state(self, stop_event : Event):
        while not stop_event.is_set():
            currentTime = time.time()
            if currentTime - self.timeRead > timeout:
                self.ee.emit("pause")
                self.currentId = 0
            elif self.newId != self.currentId:
                self.currentId = self.newId
                self.ee.emit("start", self.currentId)
            time.sleep(1)

    def read_rfid(self, stop_event : Event):
        while not stop_event.is_set():
            self.newId, = self.reader.read()
            print(f"ID read: {self.newId}")
            self.timeRead = time.time()
            time.sleep(1)

