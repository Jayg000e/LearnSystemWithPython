from multiprocessing import Process, Value
import time
import ctypes

# Function to modify shared value
def modify_shared_value(shared_value):
    print(f"Value before modification: {shared_value.value}")
    shared_value.value = 10
    print(f"Value after modification: {shared_value.value}")

# Function to read shared value
def read_shared_value(shared_value):
    print(f"Waiting for modification...")
    time.sleep(2)  # Wait to ensure the value is modified by the other process
    print(f"Value read: {shared_value.value}")

if __name__ == '__main__':
    # Create a shared value of type 'int' (i)
    shared_value = Value(ctypes.c_int, 0)

    # Create a process that will modify the shared value
    p1 = Process(target=modify_shared_value, args=(shared_value,))

    # Create another process that will read the shared value
    p2 = Process(target=read_shared_value, args=(shared_value,))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()
