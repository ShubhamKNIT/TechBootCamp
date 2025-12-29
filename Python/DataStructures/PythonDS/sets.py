# Demonstrating basic set operations in Python
# Sets are unordered collections of unique elements.

basket_1 = {'apple', 'banana', 'cherry'}
basket_2 = {'banana', 'dragonfruit', 'elderberry'}

# Indexing and slicing are not supported in sets
# print(basket_1[0])  # This will raise an error

# Looping through a set
print("Elements in basket_1:")
for item in basket_1:
    print(item, end=', ')

# Checking membership
print("\nIs 'apple' in basket_1?", 'apple' in basket_1)

# Add elements
basket_1.add('date')
print("After adding 'date' to basket_1:", basket_1)

# Remove elements
basket_1.remove('cherry')
print("After removing 'cherry' from basket_1:", basket_1)

# Update set with multiple elements using list via update()
basket_1.update(['fig', 'grape'])
print("After updating basket_1 with ['fig', 'grape']:", basket_1)

# Set operations
union_set = basket_1 | basket_2 # or basket_1.union(basket_2)
print("Union of basket_1 and basket_2:", union_set)

intersection_set = basket_1 & basket_2 # or basket_1.intersection(basket_2)
print("Intersection of basket_1 and basket_2:", intersection_set)

difference_set = basket_1 - basket_2 # or basket_1.difference(basket_2)
print("Difference of basket_1 and basket_2 (basket_1 - basket_2):", difference_set)

symmetric_difference_set = basket_1 ^ basket_2 # or basket_1.symmetric_difference(basket_2)
print("Symmetric Difference of basket_1 and basket_2:", symmetric_difference_set)

# FROZEN SET (immutable set)
frozen_basket = frozenset(['kiwi', 'lemon', 'mango'])
print("Frozen set:", frozen_basket)
try:
    frozen_basket.add('nectarine')  # This will raise an error
except AttributeError as e:
    print("Error:", e)

# set methods
# 1. add() - Adds an element to the set.
# 2. remove() - Removes a specified element from the set.
# 3. discard() - Removes a specified element if it is present in the set.
# 4. pop() - Removes and returns an arbitrary element from the set.
# 5. clear() - Removes all elements from the set.
# 6. union() - Returns a new set with elements from both sets.
# 7. intersection() - Returns a new set with elements common to both sets.
# 8. difference() - Returns a new set with elements in the set that are not in the other set.
# 9. symmetric_difference() - Returns a new set with elements in either set but not in both.
# 10. update() - Updates the set with elements from another iterable (like list, set, etc.).
# 11. isdisjoint() - Returns True if two sets have no elements in common.
# 12. issubset() - Returns True if the set is a subset of another
# 13. issuperset() - Returns True if the set is a superset of another