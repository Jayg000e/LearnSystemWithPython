import threading

class DiningPhilosophers:
    def __init__(self):
        self.state = ['THINKING'] * 5
        self.lock = threading.Lock()
        self.self_condition = [threading.Condition(self.lock) for _ in range(5)]

    def pickup(self, i):
        with self.lock:
            self.state[i] = 'HUNGRY'
            self.test(i)
            if self.state[i] != 'EATING':
                self.self_condition[i].wait()

    def putdown(self, i):
        with self.lock:
            self.state[i] = 'THINKING'
            self.test((i + 4) % 5)
            self.test((i + 1) % 5)

    def test(self, i):
        if self.state[(i + 4) % 5] != 'EATING' and self.state[i] == 'HUNGRY' and self.state[(i + 1) % 5] != 'EATING':
            self.state[i] = 'EATING'
            self.self_condition[i].notify()

def philosopher_task(id, diningPhilosophers):
    for _ in range(10):  # Each philosopher eats 10 times
        # Think
        print(f'Philosopher {id} is thinking.')
        # Pickup chopsticks
        diningPhilosophers.pickup(id)
        # Eat
        print(f'Philosopher {id} is eating.')
        # Putdown chopsticks
        diningPhilosophers.putdown(id)

if __name__ == "__main__":
    diningPhilosophers = DiningPhilosophers()
    philosophers = [threading.Thread(target=philosopher_task, args=(i, diningPhilosophers)) for i in range(5)]
    
    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()
