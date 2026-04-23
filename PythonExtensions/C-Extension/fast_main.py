import time
from threading import Thread
from fast_factorial_module import factorial_with_GIL as factorial


def worker(n, n_reps):
    factorial(n, n_reps)


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