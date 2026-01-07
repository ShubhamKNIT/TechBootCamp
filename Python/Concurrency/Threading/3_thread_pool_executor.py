from asyncio import as_completed
import time
import concurrent.futures

start_time = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds} seconds"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # Submit multiple tasks to the executor - Return futures object
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)

#     # Retrieve results using future.result()
#     print(f1.result())
#     print(f2.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:

#     # Using a loop to submit 10 tasks to the executor
#     secs = [1, 4, 5, 2, 3]
#     results = [executor.submit(do_something, sec) for sec in secs]

#     # Retrieve results as they complete in any order
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Using executor.map() to submit multiple tasks
    secs = [1, 4, 5, 2, 3]
    results = executor.map(do_something, secs)

    # Retrieve results in the order tasks were submitted
    for result in results:
        print(result)

end_time = time.perf_counter()

print(f"Finished in {round(end_time - start_time, 2)} second(s)")