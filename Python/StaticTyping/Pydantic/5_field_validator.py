# Custom field validation and transformation

from typing import List, Optional, Dict
from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        # valid-email = username@hdfc.com or username@icici.com
        domain_name = value.lower().split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        

    # Mode is important as it allows transformation 
    # before or after (default) type coercion or checking
    @field_validator('name')
    @classmethod
    def name_transformer(cls, value):
        return value.upper()

    # 3. age positive integer check   
    # raise error before type coercion
    # @field_validator('age', mode='before')

    # no error -> pydantic auto converts str to int for number fields
    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else: 
            raise ValueError('Age must be positive integer')

patient = Patient(
    name="Alice Smith",

    # 2. email custom field validation
    email="alice@hdfc.com",
    # email="alice@smith.com",

    age=24,
    # 3. age string auto conversion check
    # age="24",

    weight=70,
    contact_details={"address": "Jane Street, New Jersey, USA"}
)

print(patient.model_dump_json(indent=4))