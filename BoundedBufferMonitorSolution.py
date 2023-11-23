import threading

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            self.not_full.notify()
            return item

# Example usage
bounded_buffer = BoundedBuffer(10)

def producer():
    for i in range(20):
        bounded_buffer.put(i)
        print(f"Produced: {i}")

def consumer():
    for i in range(20):
        item = bounded_buffer.get()
        print(f"Consumed: {item}")

# Starting Producer and Consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
