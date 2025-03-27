import time
from AI_model import Model
from User import User
from QueryBuffer import QueryBuffer
from AnswerBuffer import AnswerBuffer

class App:
    def __init__(self):
        self.QBuffer = QueryBuffer(5)
        self.ABuffer = AnswerBuffer(5)

        self.model = Model(self.QBuffer, self.ABuffer)

        self.users = []
        for i in range(5):
            self.users.append(User(self.QBuffer, self.ABuffer, i))

    def start_threads(self):        
        for user in self.users:
            user.sendRequests()
        
        self.model.answerRequests()

    def interrupt_threads(self):
        for user in self.users:
            user.interruptRequests()
            try:
                user.joinThreads()
            except InterruptedError as e:
                e.with_traceback()

        self.model.interruptAnswer()
        try:
            self.model.joinThreads()
        except InterruptedError as e:
            e.with_traceback()
        
        print("Query Buffer: " + str(self.QBuffer.show()))
        print("Answer Buffer: " + str(self.ABuffer.show()))

    def run(self):
        self.start_threads()

        try:
            time.sleep(30)
        except InterruptedError as e:
            e.with_traceback()

        self.interrupt_threads()

if __name__ == "__main__":
    app = App()
    app.run()
