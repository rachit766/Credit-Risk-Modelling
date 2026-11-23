
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prediction_helper import predict

app = FastAPI(title="Credit Risk Modelling API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CreditData(BaseModel):
    age: int
    income: float
    loan_amount: float
    loan_tenure_months: int
    avg_dpd_per_delinquency: float
    delinquency_ratio: float
    credit_utilization_ratio: float
    num_open_accounts: int
    residence_type: str
    loan_purpose: str
    loan_type: str

@app.get("/")
def home():
    return {"message": "Credit Risk API is running"}

@app.post("/predict")
def predict_risk(data: CreditData):
    probability, credit_score, rating = predict(
        data.age, data.income, data.loan_amount,
        data.loan_tenure_months, data.avg_dpd_per_delinquency,
        data.delinquency_ratio, data.credit_utilization_ratio,
        data.num_open_accounts, data.residence_type,
        data.loan_purpose, data.loan_type
    )

    loan_to_income_ratio = (
        data.loan_amount / data.income if data.income > 0 else 0
    )

    return {
        "default_probability": float(probability),
        "credit_score": int(credit_score),
        "rating": rating,
        "loan_to_income_ratio": float(loan_to_income_ratio)
    }
