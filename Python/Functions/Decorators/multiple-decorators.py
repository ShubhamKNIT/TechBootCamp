import functools

def apply_uppercase(func):
    @functools.wraps(func)
    def wrapper(*args):
        res = func(*args)
        return res.upper()
    return wrapper

def apply_splitting(func):
    @functools.wraps(func)
    def wrapper(*args):
        res = func(*args)
        return res.split(", ")
    return wrapper

@apply_splitting
@apply_uppercase
def say_hello(greet):
    return greet

if __name__ == "__main__":
    print(say_hello("Hello, fray"))