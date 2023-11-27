import multiprocessing
import random
import time

def resource_manager(name, command_queue, vote_queue, ready_event):
    while True:
        command = command_queue.get()
        if command == 'PREPARE':
            # Wait for a signal to start preparation
            ready_event.wait()
            ready_event.clear()  # Clear the event for the next round

            # Simulate preparation with a random success or failure
            prepared = random.choice([True, False])  # Randomly choose True or False
            print(f"{name} is preparing... {'success' if prepared else 'failure'}")
            vote_queue.put(('YES' if prepared else 'NO', name))
        elif command == 'COMMIT':
            print(f"{name} commits.")
            break
        elif command == 'ABORT':
            print(f"{name} aborts.")
            # Continue to the next iteration for a possible retry

def transaction_coordinator(rm_count):
    command_queues = [multiprocessing.Queue() for _ in range(rm_count)]
    vote_queue = multiprocessing.Queue()
    ready_events = [multiprocessing.Event() for _ in range(rm_count)]

    # Start resource managers
    rms = [multiprocessing.Process(target=resource_manager, args=(f"RM{i}", command_queues[i], vote_queue, ready_events[i])) for i in range(rm_count)]
    for rm in rms:
        rm.start()

    attempt = 0
    while True:
        print(f"Attempt {attempt + 1}")
        attempt += 1

        # Signal RMs to prepare
        for event in ready_events:
            event.set()

        # Phase 1: Send prepare command
        for q in command_queues:
            q.put('PREPARE')

        # Collect votes
        votes = [vote_queue.get() for _ in range(rm_count)]

        # Phase 2: Decide to commit or abort
        if all(vote == 'YES' for vote, _ in votes):
            print("All resource managers are ready. Sending COMMIT command.")
            for q in command_queues:
                q.put('COMMIT')
            break
        else:
            print("One or more resource managers are not ready. Sending ABORT command and retrying.")
            for q in command_queues:
                q.put('ABORT')
            time.sleep(0.5)  # Wait for a bit before retrying

    # Wait for all RMs to finish
    for rm in rms:
        rm.join()

if __name__ == '__main__':
    transaction_coordinator(2)
