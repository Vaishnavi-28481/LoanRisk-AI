from sqlalchemy.orm import Session
from api import models


def save_prediction(db: Session, data, prediction, probability):

    record = models.PredictionHistory(

        Gender=data.Gender,
        Married=data.Married,
        Dependents=data.Dependents,
        Education=data.Education,
        Self_Employed=data.Self_Employed,

        ApplicantIncome=data.ApplicantIncome,
        CoapplicantIncome=data.CoapplicantIncome,
        LoanAmount=data.LoanAmount,
        Loan_Amount_Term=data.Loan_Amount_Term,

        Credit_History=data.Credit_History,

        Property_Area_Semiurban=data.Property_Area_Semiurban,
        Property_Area_Urban=data.Property_Area_Urban,

        Prediction=prediction,
        Probability=probability
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record