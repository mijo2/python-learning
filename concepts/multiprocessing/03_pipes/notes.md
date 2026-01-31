# Pipes in Multiprocessing

## Overview
Pipes provide a way for processes to communicate by sending and receiving data. They create a connection between two processes, allowing bidirectional or unidirectional communication.

## Basic Pipe Usage
```python
from multiprocessing import Pipe, Process
import time

def sender(conn):
    for i in range(5):
        conn.send(f"Message {i}")
        time.sleep(0.1)
    conn.send(None)  # Signal end
    conn.close()

def receiver(conn):
    while True:
        msg = conn.recv()
        if msg is None:
            break
        print(f"Received: {msg}")
    conn.close()

parent_conn, child_conn = Pipe()

sender_proc = Process(target=sender, args=(child_conn,))
receiver_proc = Process(target=receiver, args=(parent_conn,))

sender_proc.start()
receiver_proc.start()

sender_proc.join()
receiver_proc.join()
```

## Pipe Types
- **Duplex Pipes**: Bidirectional communication
- **Half-duplex**: One-way communication
- **Named Pipes**: FIFO files for process communication

## Pipe Methods
- **send(obj)**: Send Python object
- **recv()**: Receive Python object
- **close()**: Close pipe connection
- **poll(timeout)**: Check if data available

## Advanced Patterns
```python
# Request-response pattern
def worker(pipe):
    while True:
        request = pipe.recv()
        if request == "quit":
            break
        result = process_request(request)
        pipe.send(result)

# Duplex communication
parent_conn, child_conn = Pipe(duplex=True)

# Send complex objects
data = {"numbers": [1, 2, 3], "text": "hello"}
parent_conn.send(data)
received = child_conn.recv()
```

## Performance Considerations
- **Serialization**: Objects pickled for transfer
- **Buffer Size**: Internal buffering affects performance
- **Blocking**: send/recv can block
- **Throughput**: Pipes have overhead

## Error Handling
```python
try:
    data = conn.recv()
except EOFError:
    print("Connection closed")
except Exception as e:
    print(f"Pipe error: {e}")
finally:
    conn.close()
```

## Use Cases
- **Process Communication**: Send results between processes
- **Worker Processes**: Master-worker architectures
- **Data Streaming**: Stream data between processes
- **RPC Systems**: Remote procedure calls

## Limitations
- **Two Processes**: Pipes connect exactly two processes
- **No Broadcasting**: Can't send to multiple recipients
- **Process Lifetime**: Pipes close when processes exit
- **Memory**: Large objects increase memory usage

## Best Practices
- Close pipes explicitly
- Handle connection errors
- Use timeouts for robustness
- Serialize efficiently
- Monitor pipe usage
