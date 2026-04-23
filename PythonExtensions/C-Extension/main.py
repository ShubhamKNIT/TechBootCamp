import time
from threading import Thread


def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def worker(n, n_reps):
    for _ in range(n_reps):
        factorial(n)


if __name__ == "__main__":

    threads = [
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000)),
        Thread(target=worker, args=(20, 5_000_000))
    ]

    start = time.perf_counter()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()

    print(f"Execution time: {end - start:.6f} seconds")