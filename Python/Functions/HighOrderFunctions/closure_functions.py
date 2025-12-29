# What is a closure function?
# A closure function is a nested function that
# captures the variables from its enclosing scope.
# This allows the nested function to remember the state of those
# variables even after the outer function has finished executing.

# When to use closure functions?
# 1. Data Encapsulation: Closures can be used to encapsulate data,
#    providing a way to create private variables.
# 2. Factory Functions: They can be used to create function factories,
#    where the outer function generates and returns a customized inner function.
# 3. Maintaining State: Closures can maintain state across multiple calls
#    without using global variables or class instances.

def get_counter():
    """
    Returns a closure that counts the number of times it has been called.
    Each call to the returned function increments and returns the count.
    Every call to get_counter() creates a new independent counter.
    """
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

if __name__ == "__main__":
    counter_1 = get_counter()
    counter_2 = get_counter()

    print(counter_1())  # Output: 1
    print(counter_1())  # Output: 2
    print(counter_2())  # Output: 1
