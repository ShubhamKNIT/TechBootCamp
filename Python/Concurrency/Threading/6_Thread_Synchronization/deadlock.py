# Deadlock Condition:
# 1. Mutual Exclusion: At least one resource must be held in a non-sharable mode.
# 2. Hold and Wait: A thread holding at least one resource is waiting to acquire
#    additional resources held by other threads.
# 3. No Preemption: Resources cannot be forcibly removed from threads holding them.
# 4. Circular Wait: A set of threads are waiting for each other in a circular

# NOTE: This code is for demonstration purposes only. Running this code will result in a deadlock.
# and the program will hang indefinitely.
# Terminate the program manually to stop it.

import threading
import time

# Create two locks
lock_A = threading.Lock()
lock_B = threading.Lock()

def thread_1():
    print("Thread 1: Acquiring Lock A...")
    lock_A.acquire()
    time.sleep(1)  # Simulate some processing time
    print("Thread 1: Acquired Lock A, trying to acquire Lock B...")
    lock_B.acquire()  # Wait for Lock B
    print("Thread 1: Acquired Lock B, performing task.")
    lock_B.release()
    lock_A.release()

def thread_2():
    print("Thread 2: Acquiring Lock B...")
    lock_B.acquire()
    time.sleep(1)  # Simulate some processing time
    print("Thread 2: Acquired Lock B, trying to acquire Lock A...")
    lock_A.acquire()  # Wait for Lock A
    print("Thread 2: Acquired Lock A, performing task.")
    lock_A.release()
    lock_B.release()

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
