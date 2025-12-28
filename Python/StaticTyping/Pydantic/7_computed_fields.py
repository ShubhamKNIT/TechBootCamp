from typing import List, Optional, Dict
from pydantic import BaseModel, EmailStr, computed_field

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100  # Convert height from cm to meters
        return round(self.weight / (height_in_meters ** 2), 2)
    
patient = Patient(
    name="Alice Smith",
    email="alice@hdfc.com",
    age=12, 
    weight=70,
    height=170,
    contact_details={"address": "Jane Street, New Jersey, USA", 'emergency_contact': 'Bob Smith - 1234567890'}
)

print(patient.model_dump_json(indent=4))