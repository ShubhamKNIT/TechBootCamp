# Context Manager - It allows proper acquisition and release of resources.
# Usage: To manage resources like file streams, network connections, etc., ensuring they are properly cleaned up after use.

with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    print("Data written to 'example.txt'.")