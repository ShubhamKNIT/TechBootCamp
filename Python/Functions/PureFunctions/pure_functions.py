# Pure Functions in Python

# A pure function is a function that, 
# given the same input,
# will always return the same output.

# It does not have side effects,
# meaning it does not modify 
# any external state or variables.

# Why use pure functions?
# 1. Predictability: Easier to understand and reason about.
# 2. Testability: Easier to test since they depend only on input parameters.
# 3. Reusability: Can be reused in different contexts without side effects.

def add(a, b):
    """A pure function that adds two numbers."""
    return a + b

def append_to_list(lst, item):
    """A pure function that returns a new list with the item appended."""
    # return lst + [item]
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst