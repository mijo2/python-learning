# Interprocess Communication Patterns

## Overview
Effective interprocess communication (IPC) is crucial for multiprocessing applications. Different patterns serve different use cases, from simple request-response to complex distributed systems.

## Request-Response Pattern
```python
from multiprocessing import Process, Pipe

def server(conn):
    while True:
        request = conn.recv()
        if request == "quit":
            break
        response = process_request(request)
        conn.send(response)

def client(conn):
    requests = ["request1", "request2", "quit"]
    for req in requests:
        conn.send(req)
        if req != "quit":
            response = conn.recv()
            print(f"Response: {response}")

parent_conn, child_conn = Pipe()
server_proc = Process(target=server, args=(child_conn,))
client_proc = Process(target=client, args=(parent_conn,))

server_proc.start()
client_proc.start()
server_proc.join()
client_proc.join()
```

## Producer-Consumer Pattern
```python
from multiprocessing import Process, Queue

def producer(q, items):
    for item in items:
        q.put(item)
        print(f"Produced {item}")

def consumer(q, consumer_id):
    while True:
        item = q.get()
        if item is None:  # Sentinel value
            q.put(None)  # Re-signal for other consumers
            break
        process_item(item)
        print(f"Consumer {consumer_id} processed {item}")

queue = Queue()
items = range(10)

producer_proc = Process(target=producer, args=(queue, items))
consumer_procs = [Process(target=consumer, args=(queue, i)) for i in range(3)]

producer_proc.start()
for p in consumer_procs: p.start()

producer_proc.join()
for _ in consumer_procs: queue.put(None)
for p in consumer_procs: p.join()
```

## Master-Worker Pattern
```python
from multiprocessing import Pool

def worker_task(task_data):
    # Process task
    return f"Processed {task_data}"

tasks = range(100)

with Pool(processes=4) as pool:
    results = pool.map(worker_task, tasks)
```

## Pipeline Pattern
```python
def stage1(data):
    # First processing stage
    return [x * 2 for x in data]

def stage2(data):
    # Second processing stage
    return [x + 1 for x in data]

def stage3(data):
    # Final processing stage
    return sum(data)

# Sequential pipeline
data = list(range(10))
result1 = stage1(data)
result2 = stage2(result1)
final_result = stage3(result2)

# Parallel pipeline with queues
from multiprocessing import Process, Queue

def pipeline_stage(input_q, output_q, func):
    while True:
        item = input_q.get()
        if item is None:
            output_q.put(None)
            break
        result = func(item)
        output_q.put(result)
```

## Publish-Subscribe Pattern
```python
from multiprocessing import Manager

manager = Manager()
subscribers = manager.list()

def publisher():
    for i in range(5):
        message = f"Message {i}"
        for callback in subscribers:
            callback(message)

def subscriber(name, callback):
    subscribers.append(callback)
    # Listen for messages

# Usage
def my_callback(msg):
    print(f"Subscriber received: {msg}")

subscriber("sub1", my_callback)
publisher()
```

## Event-Driven Pattern
```python
from multiprocessing import Event, Process

event = Event()

def waiter():
    print("Waiting for event")
    event.wait()  # Blocks until event is set
    print("Event received")

def setter():
    import time
    time.sleep(2)
    event.set()  # Trigger event

wait_proc = Process(target=waiter)
set_proc = Process(target=setter)

wait_proc.start()
set_proc.start()
wait_proc.join()
set_proc.join()
```

## Synchronization Patterns
- **Barriers**: All processes wait at synchronization point
- **Semaphores**: Control access to shared resources
- **Locks**: Mutual exclusion for critical sections
- **Conditions**: Wait for specific conditions

## Error Handling Patterns
```python
def robust_worker(q):
    try:
        while True:
            try:
                item = q.get(timeout=1)
                result = process_item(item)
                results_q.put(result)
            except queue.Empty:
                continue
            except Exception as e:
                error_q.put((item, str(e)))
    except KeyboardInterrupt:
        pass  # Graceful shutdown
```

## Best Practices
- Choose appropriate communication mechanism
- Handle process failures gracefully
- Use timeouts to prevent deadlocks
- Monitor communication patterns
- Test with different numbers of processes
