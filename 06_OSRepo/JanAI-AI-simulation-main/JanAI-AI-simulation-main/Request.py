import threading
import random

class Request(threading.Thread):
    def __init__(self, QBuffer, ABuffer, usID, reqID):
        super().__init__()
        self._stop_event = threading.Event()
        self.query = QBuffer
        self.answer = ABuffer
        self.userID = usID
        self.reqID = reqID
        self.reqData = []

    def run(self):
        try:
            self.reqData = [self.userID, self.reqID, random.randint(1, 50)]
            
            self.query.add(self.reqData)

            item = self.answer.remove(self.reqData)
            print(str(item[0]) + " RECEIVED ANSWER FROM ANSWERBUFFER: " + str(item[2]) + "\n")

        except InterruptedError as e:
            print(f"Error in REQUEST thread {self.name}: {e}")
            self.end = True

    def interrupt(self):
        self._stop_event.set()