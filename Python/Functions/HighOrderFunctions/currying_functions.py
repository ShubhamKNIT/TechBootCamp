# What is Currying Functions?
# Function currying is a specific kind of function transformation 
# where we translate a single function that accepts multiple arguments 
# into multiple functions that each accept a single argument.

# When to use currying functions?
# 1. Partial Application: Currying allows for partial application of functions,
#    enabling you to fix a certain number of arguments and generate a new function.
# 2. Function Reusability: It enhances function reusability by allowing you to
#    create specialized functions from general ones.
# 3. Improved Readability: Currying can improve code readability by breaking down
#    complex functions into simpler, single-argument functions.
from functools import reduce

def box_volume(length):
    """
    Returns a curried function to calculate the volume of a box.
    Usage: box_volume(length)(width)(height)
    """
    def box_volume_with_len(width):
        def box_volume_with_width(height):
            return length * width * height
        return box_volume_with_width
    return box_volume_with_len

print("Volume of box: ", box_volume(3)(4)(5))

def line_with_sequence(char):
    """
    Returns a curried function to count lines containing a specific sequence of characters.
    Usage: line_with_sequence(char)(length)(document)
    """
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.split("\n")
            return reduce(lambda acc, line : acc + 1 if sequence in line else acc, lines, 0)

        return with_length
    return with_char

DOC = """Hello World
This is a sample document.
***
This line has three stars: ***
This line does not.
*** Another line with stars: ***
End of document."""
print("Number of lines with '***': ", line_with_sequence('*')(3)(DOC))