import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        for _ in range(10):  # Repeat the eat-think cycle 10 times
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.uniform(1, 3))  # Simulate thinking

    def eat(self):
        # Try to pick up the forks (semaphores) starting with the left one
        self.left_fork.acquire()
        self.right_fork.acquire()

        print(f"Philosopher {self.index} is eating.")
        time.sleep(random.uniform(1, 3))  # Simulate eating

        # Put down the forks (release the semaphores)
        self.left_fork.release()
        self.right_fork.release()

def main():
    # Create 5 semaphores (one for each fork)
    forks = [threading.Semaphore() for _ in range(5)]

    # Create 5 philosophers, each philosopher will have a left and right fork
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    # Start all philosopher threads
    for p in philosophers:
        p.start()

    # Wait for all philosopher threads to finish
    for p in philosophers:
        p.join()

if __name__ == "__main__":
    main()
