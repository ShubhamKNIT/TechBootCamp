# Deadlock Prevention Example:

# This code demonstrates how to prevent deadlocks in a multithreaded environment
# by enforcing a strict order of resource acquisition.

# By ensuring that all threads acquire locks in the same order, we eliminate
# the possibility of circular wait, thus preventing deadlocks.

# Note: This code is safe to run and will not result in a deadlock.

import threading
import time

# Create two locks
lock_A = threading.Lock()
lock_B = threading.Lock()

def thread_1():
    print("Thread 1: Acquiring Lock A...")
    with lock_A:
        time.sleep(1)  # Simulate some processing time
        print("Thread 1: Acquired Lock A, trying to acquire Lock B...")
        with lock_B:
            print("Thread 1: Acquired Lock B, performing task.")
    print("Thread 1: Released Lock B and Lock A.")

def thread_2():
    print("Thread 2: Acquiring Lock A...")
    with lock_A:
        time.sleep(1)  # Simulate some processing time
        print("Thread 2: Acquired Lock A, trying to acquire Lock B...")
        with lock_B:
            print("Thread 2: Acquired Lock B, performing task.")
    print("Thread 2: Released Lock B and Lock A.")

def main():
    # Start thread 1 and thread 2
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()