# Generatord are tools for creating iterators in Python.
# They allow you to iterate through a sequence of values without
# storing the entire sequence in memory at once. This is particularly
# useful for large datasets or infinite sequences.

# Generators are defined using functions and the `yield` statement.
# Genartors are compact and memory-efficient, because they generate values on-the-fly.
# As __iter__() and __next__() are created automatically.

# Example 1: Simple Generator Function
def reverse_string(s):
    """A generator that yields characters of a string in reverse order."""
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

print("Example 1: Reverse String Generator")
for ch in reverse_string("hello"):
    print(ch)