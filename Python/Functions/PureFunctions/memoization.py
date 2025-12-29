# Referential Transparency and Memoization in Python

# A referentially transparent function is one that can be replaced
# with its output value without changing the program's behavior.

# Pure functions are referentially transparent.

# Memoization is an optimization technique used to speed up
# function calls by caching the results of expensive function calls
# and returning the cached result when the same inputs occur again.

# We will implement a simple memoization decorator
# and demonstrate its use with a recursive Fibonacci function.

import time

def timeit(func):
    """A simple timing decorator."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def memoize(func):
    """A simple memoization decorator."""
    cache = {}
    
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized_func

@memoize # Comment this line to disable memoization
def fibonacci(n):
    """A memoized function to compute Fibonacci numbers."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
@timeit
def main():
    """
    main() function to demonstrate 
    Fibonacci computation,
    with and without memoization.
    """
    print("Fibonacci numbers:")
    for i in range(20):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()