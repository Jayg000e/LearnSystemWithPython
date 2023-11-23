import threading
import time
import random

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.mutex = threading.Semaphore(1)
        self.empty = threading.Semaphore(capacity)  # initial count is the buffer capacity
        self.full = threading.Semaphore(0)          # initial count is 0

    def produce(self, item):
        self.empty.acquire()  # wait for empty slot
        self.mutex.acquire()  # enter critical section
        self.buffer.append(item)  # add item to buffer
        print(f"Produced: {item}")
        self.mutex.release()    # leave critical section
        self.full.release()     # increment count of full slots

    def consume(self):
        self.full.acquire()   # wait for full slot
        self.mutex.acquire()  # enter critical section
        item = self.buffer.pop(0)  # remove item from buffer
        print(f"Consumed: {item}")
        self.mutex.release()    # leave critical section
        self.empty.release()    # increment count of empty slots
        return item

# Example usage
buffer_size = 5
buffer = BoundedBuffer(buffer_size)

def producer():
    for i in range(20):
        buffer.produce(i)
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for i in range(20):
        item = buffer.consume()
        time.sleep(random.uniform(0.1, 0.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
