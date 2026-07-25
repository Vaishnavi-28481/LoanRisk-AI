from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from api.database import Base


class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    Gender = Column(Integer)
    Married = Column(Integer)
    Dependents = Column(Integer)
    Education = Column(Integer)
    Self_Employed = Column(Integer)

    ApplicantIncome = Column(Float)
    CoapplicantIncome = Column(Float)
    LoanAmount = Column(Float)
    Loan_Amount_Term = Column(Float)

    Credit_History = Column(Integer)

    Property_Area_Semiurban = Column(Integer)
    Property_Area_Urban = Column(Integer)

    Prediction = Column(String)
    Probability = Column(Float)

    Created_At = Column(DateTime, default=datetime.utcnow)