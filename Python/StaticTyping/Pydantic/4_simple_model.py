from typing import Dict, List, Optional
from pydantic import BaseModel, Field, EmailStr, AnyUrl

class Patient(BaseModel):
    name: str = Field(
                    min_length=2, 
                    max_length=50, 
                    title="Full Name", 
                    description="The patient's full name",
                    examples=["John Doe", "Jane Smith"]
                )
    email: EmailStr
    github_url: AnyUrl
    age: int = Field(gt=0, lt=150)
    weight: float = Field(gt=0)
    married: bool = Field(default=False)
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str, str]


patient = Patient(
    name="Alice Smith",
    email="alice@smith.com",
    github_url="https://github.com/alicesmith",
    age=30,
    weight=65.5,
    married=True,
    # allergies=["Peanuts", "Penicillin"],
    contact_details={"phone": "123-456-7890", "address": "123 Main St"},
)

print(patient.model_dump_json(indent=4))