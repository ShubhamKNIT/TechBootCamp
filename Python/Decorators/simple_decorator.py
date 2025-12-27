import time

def timeit(func):
    def wrapper(a, b):
        t1 = time.time()
        res = func(a, b)
        t2 = time.time()
        print(f"Took {t2 - t1} s")
        return res

    return wrapper

@timeit
def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(5, 7)
    print(f"Result: {result}")