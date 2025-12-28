# Traditional Python function without type validation (manual validation)
def create_user(username, email, age):
    if not isinstance(username, str):
        raise TypeError("Username must be a string")
    if not isinstance(email, str):
        raise TypeError("Invalid email format")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer")
    return {
        "username": username,
        "email": email,
        "age": age
    }

user1 = create_user("john_doe", "john@doe.com", 30)
print(user1)

user2 = create_user("jane_doe", None, -5)  # This will raise a ValueError
print(user2)

