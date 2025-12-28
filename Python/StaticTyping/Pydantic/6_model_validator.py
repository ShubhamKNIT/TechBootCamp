from typing import List, Optional, Dict
from pydantic import BaseModel, EmailStr, model_validator

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def emergency_contact_validator(cls, model):
        if (model.age < 14 or model.age > 60) and not model.contact_details.get('emergency_contact'):
            raise ValueError('Emergency contact is required for patients under 14 or over 60 years old')
        return model
    
# Raise error due to missing emergency contact
# patient = Patient(
#     name="Alice Smith",
#     email="alice@hdfc.com",
#     age=12, 
#     weight=70,
#     contact_details={"address": "Jane Street, New Jersey, USA"}
# )

patient = Patient(
    name="Alice Smith",
    email="alice@hdfc.com",
    age=12, 
    weight=70,
    contact_details={"address": "Jane Street, New Jersey, USA", 'emergency_contact': 'Bob Smith - 1234567890'}
)

print(patient.model_dump_json(indent=4))