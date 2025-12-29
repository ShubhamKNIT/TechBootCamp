# Demonstrating basic list operations in Python
# List are ordered, mutable collections that can hold a variety of data types.

sq = [1, 4, 9]

sq = sq + [16, 25]  # Concatenation
print("After concatenation:", sq)

sq.append(36)  # Adding an element
print("After appending 36:", sq)

sq.remove(1)  # Removing an element
print("After removing 1:", sq)

# Note: Slicing does not modify the original list
first_three = sq[0:3]  # Slicing
print("First three elements (slicing):", first_three)
print("Iterating through the list:")

first_three[0] = 100

print("After modifying first element of sliced list to 100:", first_three)
print("Original list remains unchanged:", sq)

# pop() vs del li[...] statement
popped_element = sq.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("List after popping the last element:", sq)

# del statement can remove elements by index or slice
del sq[3:]  # Deletes elements from index 3 to the end
print("List after deleting elements from index 3 onwards:", sq)


# Sort the original list to show it is unaffected
# sq.sort(reverse=False)

# Copying the list to preserve original before sorting
# sorted_sq = sq.copy()


# list methods
# 1. append() - Adds an element at the end of the list.
# 2. remove() - Removes the first occurrence of a specified element.
# 3. sort() - Sorts the list in ascending or descending order.
# 4. extend() - Extends the list by appending elements from another iterable.
# 5. pop() - Removes and returns the element at the specified index (default is the last element).
# 6. insert() - Inserts an element at a specified index.
# 7. clear() - Removes all elements from the list.
# 8. index() - Returns the index of the first occurrence of a specified element.
# 9. count() - Returns the number of occurrences of a specified element.
# 10. reverse() - Reverses the order of the list in place.
# 11. copy() - Returns a shallow copy of the list.
