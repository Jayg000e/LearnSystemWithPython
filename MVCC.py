import threading
import time
import copy

class DatabaseSimulator:
    def __init__(self):
        self.current_data = {'list': [], 'timestamp': time.time()}
        self.data_versions = [copy.deepcopy(self.current_data)]
        self.lock = threading.Lock()

    def read_list(self, read_timestamp):
        # Find the version of the list that was current at the read_timestamp
        for version in reversed(self.data_versions):
            if version['timestamp'] <= read_timestamp:
                return version['list']
        return None

    def write_list(self, new_entry):
        with self.lock:
            new_version = {'list': self.current_data['list'] + [new_entry], 'timestamp': time.time()}
            self.current_data = new_version
            self.data_versions.append(new_version)
            print(f"List write operation at timestamp {new_version['timestamp']} adds entry {new_entry}")

    def read_entry(self, index):
        with self.lock:
            return self.current_data['list'][index]

    def write_entry(self, index, new_value):
        with self.lock:
            self.current_data['list'][index] = new_value
            print(f"Entry write operation changes index {index} to {new_value}")

# Example usage
db = DatabaseSimulator()

# Simulate list read and entry read/write operations
def list_read_operation(read_id, delay=0):
    time.sleep(delay)
    read_timestamp = time.time()
    list_version = db.read_list(read_timestamp)
    print(f"List read operation {read_id} at timestamp {read_timestamp} sees the list: {list_version}")

def entry_read_operation(read_id, index, delay=0):
    time.sleep(delay)
    value = db.read_entry(index)
    print(f"Entry read operation {read_id} reads index {index} as {value}")

def entry_write_operation(write_id, index, value, delay=0):
    time.sleep(delay)
    db.write_entry(index, value)
    print(f"Entry write operation {write_id} completed.")

def list_write_operation(write_id, value, delay=0):
    time.sleep(delay)
    db.write_list(value)
    print(f"List write operation {write_id} completed.")

# Running the operations in threads
threads = []
threads.append(threading.Thread(target=lambda: list_read_operation(1)))
threads.append(threading.Thread(target=lambda: list_write_operation(1, 'A', delay=1)))
threads.append(threading.Thread(target=lambda: entry_read_operation(1, 0, delay=2)))
threads.append(threading.Thread(target=lambda: entry_write_operation(1, 0, 'B', delay=3)))
threads.append(threading.Thread(target=lambda: list_read_operation(2, delay=4)))

for t in threads:
    t.start()

for t in threads:
    t.join()

# Final list read
final_list_version = db.read_list(time.time())
print(f"Final list after all operations: {final_list_version}")
