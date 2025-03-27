from Request import Request
import random

class User():
    def __init__(self, QBuffer, ABuffer, id):
        super().__init__()
        self.query = QBuffer
        self.answer = ABuffer
        self.reqs = []
        self.userID = id
        self.request = None

    def sendRequests(self):
        reqNum = random.randint(1, 5)
        for i in range(reqNum):
            self.reqs.append(Request(self.query, self.answer, self.userID, i))

        for requests in self.reqs:
            requests.start()

    def interruptRequests(self):
        for requests in self.reqs:
            requests.interrupt()

    def joinThreads(self):
        for requests in self.reqs:
            requests.join()