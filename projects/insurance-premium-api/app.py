from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal, Union
import pickle
import pandas as pd
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

#human readable
@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

#machine readable
@app.get("/health")
def health_check():
    return {"status": "ok",
            "model_version": MODEL_VERSION}


#health risk assessment endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict_premium(user_input: UserInput):

    user_input = {"bmi": user_input.bmi,
        "age_group": user_input.age_group,
        "lifestyle_risk": user_input.lifestyle_risk,
        "city_tier": user_input.city_tier,
        "income_lpa": user_input.income_lpa,
        "occupation": user_input.occupation}
    
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={"response": prediction}) 
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
