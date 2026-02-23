import annotated_types
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            min_length=2,
            title="Patient Name",
            description=(
                "Give the patient name less than 50 characters "
                "and more than 2 characters"
            ),
            examples=["John Doe", "Manas"],
        ),
    ]
    age: int = Field(gt=0, lt=120)
    gender: str
    weight: Annotated[float, Field(gt=0 , strict=True)]
    allergies: Annotated[Optional[List[str]], Field(default = None,max_length=5)]
    married: Annotated[bool, Field(default=None, description="Is the patient married?", examples=[True, False])]
    email: EmailStr
    website: AnyUrl
    contact_details: Dict[str, str]


def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.allergies)

def update_patient_info(patient: Patient):
    patient.name = "Jane Doe"
    patient.age = 25
    patient.gender = "Female"
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.email)

patient_info = { 
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "weight": 100,
    "email": "johndoe@example.com",
    "website": "https://www.google.com",
    "contact_details": {
        "phone": "1234567890"
    }

}

patient1 = Patient(**patient_info)

insert_patient_info(patient1)
update_patient_info(patient1)
