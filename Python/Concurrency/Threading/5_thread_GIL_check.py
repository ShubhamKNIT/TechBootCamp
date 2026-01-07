import sys
import time
import concurrent.futures

def sum_from_n1_to_n2(n1, n2):
    total = 0
    for i in range(n1, n2 + 1):
        total += i
    return total

def get_n1_n1_lists(n, num_threads):
    length = n / num_threads
    li = [1]
    for i in range(1, num_threads):
        li.append(int(i * length) + 1)
    li.append(n)

    n1_n2_li = []
    for i in range(len(li) - 1):
        n1_n2_li.append((li[i], li[i + 1]))

    n1_n2_li[-1] = (n1_n2_li[-1][0], n)  # Adjust the last range to end at n
    return n1_n2_li

def sum_from_1_to_n(n, num_threads):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        n1_n2_lists = get_n1_n1_lists(n, num_threads)
        futures = executor.map(lambda p: sum_from_n1_to_n2(p[0], p[1]), n1_n2_lists)
        total_sum = sum(futures)    
        return total_sum

def main():
    t1 = time.perf_counter()

    # Check GIL status # Comment it out if not using python-freethreads build
    # print("GIL enabled?" , sys._is_gil_enabled()) 

    print("Calculating sum from 1 to 1,000,000,000 using 8 threads...")
    result = sum_from_1_to_n(1_000_000_000, 8)
    t2 = time.perf_counter()
    print("Result:", result)
    print(f"Completed in {t2 - t1} seconds")

if __name__ == "__main__":
    main()

    # python 4_GIL_Example.py (Standard CPython - GIL enabled)
    # Output:
    # Calculating sum from 1 to 1,000,000,000 using 8 threads...
    # Result: 500000004000000007
    # Completed in 14.731827291980153 seconds


    # python3.14t 4_GIL_Example.py (True Multithreading - non-blocing threads)
    # Output:
    # GIL enabled? False
    # Calculating sum from 1 to 1,000,000,000 using 8 threads...
    # Result: 500000004000000007
    # Completed in 4.363200124993455 seconds