import time, sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from threading import Thread, Lock, Event
from pymitter import EventEmitter

timeout=1.5

class RFIDReader:
    def __init__(self):
        self.open = True
        self.reader = SimpleMFRC522()
        self.timeRead = 0
        self.currentId = 0
        self.newId = 0
        self.ee = None
        self.stop_event = None

    def close(self):
        self.open = False
        self.reader.READER.Close_MFRC522()
        if self.stop_event:
            self.stop_event.set()

    def read_id(self) -> str:
        if self.open:
            id, _ = self.reader.read()
            return str(id)
        return "RFID reader inactive"

    def start_reading(self, ee : EventEmitter = None):
        self.ee = ee
        self.stop_event = Event()
        thread1 = Thread(target=self.read_rfid_until_stop, args=[self.stop_event])
        thread2 = Thread(target=self.check_state, args=[self.stop_event])
        thread1.start()
        thread2.start()


    def check_state(self, stop_event : Event):
        while not stop_event.is_set():
            currentTime = time.time()
            if currentTime - self.timeRead > timeout:
                self.ee.emit("pause")
                self.currentId = 0
            elif self.newId != self.currentId:
                self.currentId = self.newId
                self.ee.emit("start", self.currentId)
            time.sleep(timeout/3)

    def read_rfid_until_stop(self, stop_event : Event):
        while not stop_event.is_set():
            self.newId = self.read_id()
            print(f"ID read: {self.newId}")
            self.timeRead = time.time()
            time.sleep(timeout/3)

