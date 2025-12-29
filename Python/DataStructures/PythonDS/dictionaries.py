# Dictionaries in Python are unordered, mutable collections of key-value pairs.

# Creating a dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print("Initial dictionary:", person)

# Accessing values
print("Name:", person['name'])
print("Age:", person.get('age'))

# Get items, keys, and values
print("Items:", person.items())
print("Keys:", person.keys())
print("Values:", person.values())

# Update items
person.update({'age': 31, 'profession': 'Engineer'})
print("After update:", person)

# Add a new key-value pair
person['hobby'] = 'painting'
# Remove a key-value pair
# del person['city']
person.pop('city', None)  # Using pop with default to avoid KeyError
print("After adding hobby and removing city:", person)

# Dictionary methods
# 1. items() - Returns a view object of the dictionary's key-value pairs.
# 2. keys() - Returns a view object of the dictionary's keys.
# 3. values() - Returns a view object of the dictionary's values.
# 4. get(key, default) - Returns the value for the specified key if key is in dictionary, else default.
# 5. update(other_dict) - Updates the dictionary with the key-value pairs from other_dict.
# 6. pop(key, default) - Removes the specified key and returns the corresponding value. If key is not found, returns default if provided.
# 7. clear() - Removes all items from the dictionary.
# 8. copy() - Returns a shallow copy of the dictionary.
# 9. fromkeys(iterable, value) - Creates a new dictionary with keys from iterable and values set to value.
# 10. setdefault(key, default) - Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
# 11. popitem() - Removes and returns an last inserted (key, value) pair from the dictionary.
# 12. dict() - Creates a new dictionary.