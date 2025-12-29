# Generator expression uses () to create a generator in a more concise way.
# They are similar to list comprehensions but use parentheses instead of square brackets.

# Memory Efficiency:
# List comprehensions generate the entire list in memory, while generator expressions
# generate items one at a time and only when requested, making them more memory-efficient.

# Iterable vs Iterator:
# A list comprehension produces a list (an iterable), whereas a generator expression
# produces a generator object (an iterator). 
# Iterable can be looped over multiple times, while an iterator can be exhausted.

square_gen = (x * x for x in range(10))
print("Generator Expression for Squares:")
print(square_gen)  # This will print a generator object

print("Squares from Generator Expression:")
for square in square_gen:
    print(square)