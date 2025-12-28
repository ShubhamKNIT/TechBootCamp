import array as arr

a = arr.array('i', [1, 2, 3, 4, 5]) # Creating an array of integers
print("Initial array:", a)

print("Accessing elements:")
print("Second element:", a[1])

# Array Operations
# 1. Adding/Modifying elements
# 2. Removing/Deleting elements
# 3. Concatenation
# 4. Slicing
# 5. Iteration

# 1. Adding/Modifying elements
a.append(6)  # Adding an element at the end
print("After appending 6:", a)

a[0] = 10  # Modifying the first element
print("After modifying first element to 10:", a)

# 2. Removing/Deleting elements
a.remove(3)  # Removing element with value 3
print("After removing element 3:", a)

del a[2]  # Deleting element at index 2
print("After deleting element at index 2:", a)

# 3. Concatenation
b = arr.array('i', [7, 8, 9])
c = a + b  # Concatenating two arrays
print("After concatenation with [7, 8, 9]:", c)

# 4. Slicing
slice_a = c[1:5]  # Slicing from index 1 to
print("Sliced array (index 1 to 5):", slice_a)

# 5. Iteration
print("Iterating through the array:")
for element in c:
    print(element)