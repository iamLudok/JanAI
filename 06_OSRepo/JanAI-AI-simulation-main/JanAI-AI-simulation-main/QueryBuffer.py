import threading
import queue

class QueryBuffer:
    def __init__(self, size):
        self.mutex = threading.Lock()
        self.spaces = threading.Semaphore(size)
        self.waiting = threading.Semaphore(0)
        self.bq = queue.Queue(maxsize=size)
        self.modelReady = threading.Condition(self.mutex)

        self.end = False

    def kill_buffer(self):
        with self.mutex:
            self.end = True
            self.modelReady.notify()

    def add(self, reqData):
        self.spaces.acquire()
        with self.mutex:           
            self.bq.put(reqData)
            print(str(reqData[0]) + " ADD QUERY >  " + str(reqData[2]) + "\n")
            if self.bq.full():
                self.modelReady.notify()

    def remove(self):
        item = 0

        with self.mutex:
            if self.bq.empty():
                self.spaces.release(self.bq.maxsize)
                self.modelReady.wait(timeout=10)
            if self.end == True:
                return None
            
            item = self.bq.get()
            print(str(item[0]) + " TAKE QUERY < " + str(item[2]) + "\n")

            return item

    def show(self):
        return list(self.bq.queue)