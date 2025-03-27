import threading

class AnswerBuffer:
    def __init__(self, size):
        self.mutex = threading.Lock()
        self.spaces = threading.Semaphore(size)
        self.answerDict = {}
        self.checkBuffer = threading.Condition(self.mutex)

    def add(self, item):
        self.spaces.acquire()
        with self.mutex:
            self.answerDict[(item[0], item[1])] = [item[0], item[1], item[2]]

            print(str(item[0]) + " ADD ANSWER >  " + str(item[2]) + "\n")
            self.checkBuffer.notify_all()

    def remove(self, reqData):
        with self.mutex:
            while True:
                popped_message = self.answerDict.pop((reqData[0], reqData[1]), None)

                if popped_message is not None:
                    print(str(popped_message[0]) + " TAKE ANSWER < " + str(popped_message[2]))
                    self.spaces.release()
                    return popped_message

                self.checkBuffer.wait()

    def show(self):
        return str(self.answerDict)