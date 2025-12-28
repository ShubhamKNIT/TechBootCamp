from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

user1 = User(username="john_doe", email="john@doe.com", age=30)
print(user1)

user2 = User(username="jane_doe", email=None, age=-5)  # This will raise a validation error
print(user2)