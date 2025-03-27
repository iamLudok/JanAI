from Answer import Answer

class Model():
    def __init__(self, QBuffer, ABuffer):
        super().__init__()
        self.query = QBuffer
        self.answer = ABuffer
        self.mainAnswer = None

    def answerRequests(self):
        self.mainAnswer = Answer(self.query, self.answer)
        self.mainAnswer.start()

    def interruptAnswer(self):
        self.mainAnswer.interrupt()

    def joinThreads(self):
        self.mainAnswer.join(timeout=1)