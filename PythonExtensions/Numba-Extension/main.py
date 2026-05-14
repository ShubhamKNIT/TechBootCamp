import random
from time import time
# from numba import jit
from numba import njit
from functools import wraps

def get_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# @jit(nopython=True)
@njit(nopython=True)
def monte_carlo_pi_core(n_samples):
    acc = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            acc += 1
    return (acc / n_samples) * 4

@get_performance
def monte_carlo_pi(n_samples):
    return monte_carlo_pi_core(n_samples)

n_samples = 10**6
pi_estimate = monte_carlo_pi(n_samples)
print(f"Estimated value of pi: {pi_estimate}")