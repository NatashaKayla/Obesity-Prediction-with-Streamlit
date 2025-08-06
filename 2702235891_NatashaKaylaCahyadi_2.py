from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Literal

app = FastAPI()

model = joblib.load('rf_pred.pkl') 

class LifestyleObesity(BaseModel):
    Gender: Literal['Male', 'Female']
    Age: int
    Height: float
    Weight: float
    family_history_with_overweight: Literal['yes', 'no']
    FAVC: Literal['yes', 'no']
    FCVC: float
    NCP: float
    CAEC: Literal['Always', 'Frequently', 'Sometimes', 'no']
    SMOKE: Literal['yes', 'no']
    CH2O: float
    SCC: Literal['yes', 'no']
    FAF: float
    TUE: float
    CALC: Literal['Frequently', 'Sometimes', 'no']
    MTRANS: Literal['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking']

@app.get("/")
def read_root():
    return {"Message": "Welcome to the Obesity Prediction System API"}

@app.post('/predict')
def predict(obesity: LifestyleObesity):
    data = obesity.dict()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {'Prediction': prediction[0]}