from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com','icici.com','sbi.com']
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid domain name")
        return value
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        return value.upper() 

patient_info = { 
    "name": "Shriya",
    "age": 22,
    "weight": 50,
    "married": True,
    "allergies": [],
    "email": "shriya@hdfc.com",
    "website": "https://www.google.com",
    "contact_details": {
        "phone": "1234567890"
    }
}

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

patient2 = Patient(**patient_info)

update_patient_data(patient2)




