import time
import threading

start_time = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} seconds...")
    time.sleep(seconds)
    print("Done sleeping.")

# # Thread creation
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# # Run threads using start()
# t1.start()
# t2.start()

# # Wait for both threads to finish
# t1.join()
# t2.join()

# Using a loop to create and start 10 threads
threads = []

# Create and start 10 threads
for _ in range(10):
    # Adding argument to the thread function
    t = threading.Thread(target=do_something, args=[1.5,])
    threads.append(t)
    t.start()

# Wait for all 10 threads to finish
for t in threads:
    t.join()

end_time = time.perf_counter()

print(f"Finished in {round(end_time - start_time, 2)} second(s)")