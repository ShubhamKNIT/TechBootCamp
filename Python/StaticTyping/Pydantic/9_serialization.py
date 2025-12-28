from pydantic import BaseModel

class Address(BaseModel):
    locality: str
    city: str
    state: str
    country: str

class Patient(BaseModel):
    name: str
    email: str
    age: int
    weight: float
    married: bool = False
    address: Address

patient = Patient(
    name="Alice Smith",
    email="alice@smith.com",
    age=30,
    weight=65.5,
    address=Address(
        locality="Jane Street",
        city="New Jersey",
        state="NJ",
        country="USA"
    )
)

# Control serialization with include/exclude
# print(patient.model_dump_json(indent=4, include={'name', 'email', 'age'}))

# print(patient.model_dump_json(indent=4, exclude={'address'}))

# print(patient.model_dump_json(indent=4, exclude={'address': {'locality', 'city'}}))

# Exclude unset fields
print(patient.model_dump_json(indent=4, exclude_unset=True))