# Race Condition Example with Thread Synchronization using Lock

# This code demonstrates how to prevent race conditions in a multithreaded environment
# by using a threading Lock to synchronize access to a shared variable (price).

# By acquiring a lock before modifying the shared resource and releasing it afterward,
# we ensure that only one thread can modify the variable at a time, leading to consistent
# and expected results.

# USING LOCKS NORMALLY
# lock = threading.Lock() # Create a lock object
# lock.acquire()        # Acquire the lock before accessing the shared resource
# # Critical section of code that modifies the shared resource
# lock.release()        # Release the lock after accessing the shared resource

# USING LOCKS WITH 'WITH' STATEMENT (CONTEXT MANAGER - RECOMMENDED)
# with lock:            # Automatically acquires the lock
#   Critical section of code that modifies the shared resource
# # Lock is automatically released when exiting the 'with' block

import time
import threading

global start 
start = time.perf_counter()
lock = threading.Lock() # Global lock object - Shared among threads

def stock_raise_1(thread_id, price):
    with lock:
        price[0] += 200
        time_delta = time.perf_counter() - start
        print(f"Thread ID: {thread_id}")
        print(f"Stock price increased to: {price[0]}")
        print(f"Time taken: {time_delta}")

def stock_raise_2(thread_id, price):
    with lock:
        price[0] += 300
        time_delta = time.perf_counter() - start
        print(f"Thread ID: {thread_id}")
        print(f"Stock price increased to: {price[0]}")
        print(f"Time taken: {time_delta}")

def main(price):
    threads = []
    for i in range(1, 5):
        threads.append(threading.Thread(target=stock_raise_1 if i % 2 == 1 else stock_raise_2, args=(i, price)))

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return price[0]

if __name__ == "__main__":
    PRICE = [500]
    print(f"Final stock price: {main(PRICE)}")

# O/P:
# Thread ID: 1
# Stock price increased to: 700
# Time taken: 0.00011100000119768083
# Thread ID: 2
# Stock price increased to: 1000
# Time taken: 0.0003031250016647391
# Thread ID: 3
# Stock price increased to: 1200
# Time taken: 0.00041245800093747675
# Thread ID: 4
# Stock price increased to: 1500
# Time taken: 0.00043362500218790956
# Final stock price: 1500