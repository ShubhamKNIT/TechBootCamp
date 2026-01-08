# Race Condition without Synchronization
# In this example, multiple threads attempt to modify a shared variable (price) without any synchronization
# mechanisms in place. This can lead to inconsistent and unexpected results, demonstrating
# the concept of race conditions in multithreaded programming.

# Key Aspects of Race Conditions Demonstrated:
# 1. Concurrent Access: Multiple threads access and modify the shared resource (price) simultaneously.
# 2. Shared State: The shared variable (price) is not protected, allowing threads to read and write its value concurrently.
# 3. Timing/Order of Execution: The order in which threads execute can vary, leading to different outcomes based on timing.
# 4. Atomicity Violation: The operations on the shared variable are not atomic, meaning they can be interrupted by other threads.

# Key Characteristics of the Race Condition:
# - Inconsistent Results: The final value of the shared variable (price) may not reflect 
#   all the increments made by the threads, leading to unexpected results.
# - Non-Deterministic Behavior: The outcome can vary between runs due to the unpredictable
#   timing of thread execution.
# - Dependency on Thread Scheduling: The behavior of the program can depend on how the operating
#   system schedules the threads, which can differ across executions.
# - Difficult to detect and Debug: Race conditions can be subtle and hard to reproduce, making them challenging to identify and fix.

import time
import threading

global start 
start = time.perf_counter()

def stock_raise_1(thread_id, price):
    price[0] += 200
    time_delta = time.perf_counter() - start
    print(f"Thread ID: {thread_id}")
    print(f"Stock price increased to: {price[0]}")
    print(f"Time taken: {time_delta}")

def stock_raise_2(thread_id, price):
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
# Stock price increased to: 1000
# Thread ID: 2
# Stock price increased to: 1500
# Thread ID: 3
# Stock price increased to: 1500
# Thread ID: 4
# Stock price increased to: 1500
# Time taken: 0.00031916700027068146
# Time taken: 0.00010483400183147751
# Time taken: 0.00025312499928986654
# Time taken: 0.00017750000188243575
# Final stock price: 1500