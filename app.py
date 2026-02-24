from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Union
import pickle
import pandas as pd

#import the ml model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

#pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., ge=0, le=120, description="Age of the user in years")]
    weight: Annotated[float, Field(..., ge=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., ge=0, le=2.5, description="Height of the user in meters")]
    income_lpa: Annotated[float, Field(..., ge=0, description="Income of the user in LPA")]
    smoker: Annotated[bool, Field(..., description="Whether the user is a smoker")]
    city: Annotated[str, Field(..., description="City of the user")]
    occupation: Annotated[Literal["retired", "freelancer", "student", "government_job", "business_owner", "private_job", "unemployed"], Field(..., description="Occupation of the user")]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height * self.height)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        return "low"
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age<25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age<60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

#health risk assessment endpoint
@app.post("/predict")
def predict_premium(user_input: UserInput):
    #convert user input to dataframe
    user_df = pd.DataFrame(
        [{"bmi": user_input.bmi,
        "age_group": user_input.age_group,
        "lifestyle_risk": user_input.lifestyle_risk,
        "city_tier": user_input.city_tier,
        "income_lpa": user_input.income_lpa,
        "occupation": user_input.occupation}]
    )
    

    #make prediction
    prediction = model.predict(user_df)[0]
    
    #return prediction
    return JSONResponse(status_code=200, content={"predicted_premium": prediction})