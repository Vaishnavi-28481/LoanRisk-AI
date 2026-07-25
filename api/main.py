from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import pandas as pd
import joblib

from api.database import engine, Base, get_db
from api import models
from api import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

model = joblib.load("models/loan_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")


class LoanApplication(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: int
    Property_Area_Semiurban: int
    Property_Area_Urban: int


@app.get("/")
def home():
    return {
        "message": "Loan Default Risk Prediction API"
    }


@app.post("/predict")
def predict(
    data: LoanApplication,
    db: Session = Depends(get_db)
):

    input_data = pd.DataFrame([data.model_dump()])
    input_data = input_data[feature_names]

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        result = "Approved"
        prob = float(probability[0][1])
    else:
        result = "Rejected"
        prob = float(probability[0][0])

    crud.save_prediction(
        db=db,
        data=data,
        prediction=result,
        probability=prob
    )

    return {
        "Prediction": result,
        "Probability": prob
    }