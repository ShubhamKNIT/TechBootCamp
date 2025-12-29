# What is Transformation Functions?
# Transformation functions are higher-order functions that
# take some parameters and return a new function
# This new function applies a specific transformation or pattern to its input.

# Why Use Transformation Functions?
# 1. Code Reusability: They allow you to create reusable functions
# that can be customized with different patterns.
# 2. Separation of Concerns: They help separate the logic
# of defining a pattern from the logic of applying that pattern.
# 3. Flexibility: They enable you to create a variety of functions
# from a single template.


def formatter(pattern):
    """
    Returns a function that formats a given text according to the specified pattern.
    The pattern should contain '{}' as a placeholder for the text.
    """
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == "{}":
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func

if __name__ == "__main__":
    bold_formatter = formatter("**{}**")
    italic_formatter = formatter("*{}*")
    print(bold_formatter("Bold Text"))      # Output: **Bold Text**
    print(italic_formatter("Italic Text"))  # Output: *Italic Text*

