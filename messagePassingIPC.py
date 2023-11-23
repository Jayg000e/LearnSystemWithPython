from multiprocessing import Process, Queue
import time

def producer(queue):
    # The producing process puts messages into the queue
    for i in range(5):
        print(f'Producing {i}')
        queue.put(i)
        time.sleep(1)  # Simulate a production time

def consumer(queue):
    # The consuming process takes messages out of the queue
    time.sleep(1)  # Delay start to simulate waiting for the producer
    while True:
        msg = queue.get()  # Will wait until an item is available
        print(f'Consumed {msg}')
        if msg == 4:  # Use '4' as a sentinel value to stop the consumer
            break

if __name__ == '__main__':
    # Create a shared queue
    queue = Queue()

    # Create the producer and consumer processes
    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for both processes to complete
    producer_process.join()
    consumer_process.join()
