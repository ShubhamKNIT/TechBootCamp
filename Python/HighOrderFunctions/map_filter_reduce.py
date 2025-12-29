from functools import reduce

# f : map, filter examples
# f(function, iterable)

# Map example: Apply a function to all items in an iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map:", squared)

# Filter example: Filter items in an iterable based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# Reduce example: Apply a rolling computation to sequential pairs in an iterable
# reduce(function, iterable, [initializer])
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using reduce:", product)