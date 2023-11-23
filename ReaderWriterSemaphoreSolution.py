import threading
import time
import random

class ReadersWriters:
    def __init__(self):
        self.read_count = 0
        self.mutex = threading.Semaphore(1)
        self.rw_mutex = threading.Semaphore(1)

    def read(self, reader_id):
        with self.mutex:
            self.read_count += 1
            if self.read_count == 1:
                self.rw_mutex.acquire()

        # Reading...
        print(f"Reader {reader_id} is reading.")
        time.sleep(1)  # Simulate reading

        with self.mutex:
            self.read_count -= 1
            if self.read_count == 0:
                self.rw_mutex.release()

    def write(self, writer_id):
        self.rw_mutex.acquire()
        # Writing...
        print(f"Writer {writer_id} is writing.")
        time.sleep(1)  # Simulate writing
        self.rw_mutex.release()

def reader_task(id, readers_writers):
    for i in range(10):
        readers_writers.read(id)
        time.sleep(random.uniform(1, 3))

def writer_task(id, readers_writers):
    for i in range(10):
        readers_writers.write(id)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    readers_writers = ReadersWriters()
    readers = [threading.Thread(target=reader_task, args=(i, readers_writers)) for i in range(5)]
    writers = [threading.Thread(target=writer_task, args=(i, readers_writers)) for i in range(2)]

    for r in readers:
        r.start()

    for w in writers:
        w.start()

    for r in readers:
        r.join()

    for w in writers:
        w.join()

