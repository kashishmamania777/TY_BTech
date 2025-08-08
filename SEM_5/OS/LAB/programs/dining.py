import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Initialize a lock for each fork
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

# Philosopher class
class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = forks[index]
        self.right_fork = forks[(index + 1) % NUM_PHILOSOPHERS]

    def run(self):
        while True:
            self.think()
            self.pick_up_forks()
            self.eat()
            self.put_down_forks()

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.uniform(1, 3))  # Simulate thinking

    def pick_up_forks(self):
        # Lock forks in a specific order to prevent deadlock
        first, second = (self.left_fork, self.right_fork) if self.index % 2 == 0 else (self.right_fork, self.left_fork)
        
        first.acquire()
        print(f"Philosopher {self.index} picked up fork {first}")
        
        second.acquire()
        print(f"Philosopher {self.index} picked up fork {second}")

    def eat(self):
        print(f"Philosopher {self.index} is eating.")
        time.sleep(random.uniform(1, 2))  # Simulate eating

    def put_down_forks(self):
        # Release both forks after eating
        self.left_fork.release()
        self.right_fork.release()
        print(f"Philosopher {self.index} put down forks.")

# Create and start threads for each philosopher
philosophers = [Philosopher(i) for i in range(NUM_PHILOSOPHERS)]
for philosopher in philosophers:
    philosopher.start()
