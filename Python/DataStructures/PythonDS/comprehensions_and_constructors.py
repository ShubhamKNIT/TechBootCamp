# Constructors and Comprehensions in Python

# Constructors in Python
# Constructors are used to create data structures like lists, sets, dictionaries, and tuples.

print("Constructors in Python:")
# List Constructor
list_constructor = list((1, 2, 3, 4, 5))
print("List created using constructor:", list_constructor)

# Set Constructor
set_constructor = set([1, 2, 2, 3, 4, 4])
print("Set created using constructor (duplicates removed):", set_constructor)

# Dictionary Constructor
dict_constructor = dict([('a', 1), ('b', 2), ('c', 3)])
print("Dictionary created using constructor:", dict_constructor)

# Tuple Constructor
tuple_constructor = tuple([1, 2, 3, 4, 5])
print("Tuple created using constructor:", tuple_constructor)

# Comprehensions in Python
# Comprehensions provide a concise way to create lists, sets, or dictionaries.
# Python does not have built-in support for comprehensions for tuples,
# but you can create a tuple from a comprehension using the tuple() constructor.

print("\nComprehensions in Python:")
# List Comprehension
squares = [x**2 for x in range(10)]
print("List of squares:", squares)

# Set Comprehension
unique_squares = {x**2 for x in range(-5, 6)}
print("Set of unique squares:", unique_squares)

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}
print("Dictionary of squares:", square_dict)

# Tuple Comprehension (using tuple() constructor)
square_tuple = tuple(x**2 for x in range(5))
print("Tuple of squares:", square_tuple)


# Advanced comprehensions techniques
print("\nAdvanced Comprehensions Techniques:")
# Conditional Comprehensions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List of even squares using conditional comprehension:", even_squares)

# if-else in Comprehensions
parity = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
print("List indicating parity using if-else in comprehension:", parity)

# expression `if-else`
# `for`
# filering with `if`
result = [
    x * 2 if x % 2 == 0 else x * 3
    for x in range(10)
    if x != 5
]
print("List using if-else with filtering in comprehension:", result)

# Nested Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix using nested list comprehension:", flattened)
