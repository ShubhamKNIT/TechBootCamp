# Tuples are immutable sequences in Python that can store a collection of items.
# They are defined using parentheses () and can contain elements of different data types.

t = ('apple', 'banana', 'cherry')  # Creating a tuple
print("Initial tuple:", t)

# Accessing elements
print("First element:", t[0])

# Tuple Modifications are not allowed since they are immutable.
# Updating tuples via list (ILLEGAL operation example)
li = list(t)  # Convert tuple to list
li[1] = 'blueberry'  # Modify the list
t = tuple(li)  # Convert back to tuple
print("Modified tuple:", t)

# Unpacking tuples
fruit1, fruit2, fruit3 = t
print("Unpacked fruits:", fruit1, fruit2, fruit3)

# Tuple can iterated and sliced like lists
print("Sliced tuple (index 0 to 2):", t[0:2])

# Tuple Methods
# 1. count(): Returns the number of occurrences of a specified value.
# 2. index(): Searches the tuple for a specified value and returns its position.
print("Count of 'apple' in tuple:", t.count('apple'))
print("Index of 'cherry' in tuple:", t.index('cherry'))

# Reversing a tuple (creates a new tuple)
reversed_t = sorted(t, reverse=True)
print("Reversed tuple:", reversed_t)

# Sorting a tuple (creates a new tuple)
sorted_t = sorted(reversed_t)
print("Sorted tuple:", sorted_t)