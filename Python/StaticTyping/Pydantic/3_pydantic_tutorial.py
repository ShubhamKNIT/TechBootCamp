from datetime import datetime, UTC
from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr, ValidationError, Field
from typing import Annotated
from functools import partial
from uuid import UUID, uuid4

# 0: Basic Pydantic Model with Field Validations
class User(BaseModel):

    # 1: Using Annotated types with Field for validation and metadata
    # uid: Annotated[int, Field(gt=0, description="User ID must be a positive integer")]
    uid: UUID = Field(default_factory=uuid4)

    username: Annotated[str, Field(min_length=3, max_length=30, description="Username must be between 3 and 50 characters")]
    # email: str

    # 4. EmailStr, SecretStr, HttpUrl
    email: EmailStr
    password: SecretStr
    website: HttpUrl | None = None


    age: Annotated[int | None, Field(ge=13, le=100, description="Age must be a non-negative integer")] = None

    verified_at: datetime | None = None

    # 2: Using default_factory for dynamic default values
    # Non-callable default factory example # Throws TypeError
    # created_at: datetime = Field(default_factory=datetime.now(tz=UTC))

    # Safe way using lambda
    # Gets called at instance creation time
    # created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))

    # 3. Other way with functools.partial
    # functools.partial creates a callable with fixed arguments 
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))


    bio: str | None = None
    is_active: bool = True

    full_name: str | None = None

# 0 - 4
# try:
#     user1 = User(
#         # uid=1,
#         age=20,
#         username="john_doe",
#         email="john@doe.com",
#     )
# except ValidationError as e:
#     print("Validation Error:", e)
#     exit(1)

# # print(user)   # pretty print of model
# # print(user.model_dump())  # python dict representation
# print(user1.model_dump_json(indent=4))  # json representation

# Testing validation errors
# Providing wrong types to trigger validation errors and dev documentation links
# try:
#     user2 = User(
#         uid="Test",
#         username=None,
#         email=123,
#     )
# except ValidationError as e:
#     print("Validation Error:", e)
#     exit(1)

# 4. Valid User creation
user = User(
    username="cipher",
    email="cipher@jet.com",
    password="cipher.jet",
    age=16
)

print(user.model_dump_json(indent=2))
# print(user.password.get_secret_value())

