from multiprocessing import Process, Pipe

def sender(conn):
    """
    Function to send data through the pipe
    """
    data_to_send = ['hello', 'world', 42, None]
    for item in data_to_send:
        conn.send(item)  # Send data
        print(f"Sent: {item}")
    conn.close()  # Close the connection when done

def receiver(conn):
    """
    Function to receive data through the pipe
    """
    while True:
        try:
            data = conn.recv()  # Receive data
            print(f"Received: {data}")
            if data is None:
                break  # Exit loop if None received
        except EOFError:
            # If the sender closes the connection, an EOFError is raised
            break

if __name__ == '__main__':
    # Create a Pipe
    parent_conn, child_conn = Pipe()

    # Create two processes that will use the Pipe for communication
    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
