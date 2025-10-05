from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI(title="Insurance Quote API - Demo")

# Define input model
class QuoteRequest(BaseModel):
    age: int
    vehicle_value: float
    coverage_type: str  # "basic" or "comprehensive"

# Define the endpoint
@app.post("/quote")
def get_quote(q: QuoteRequest):
    base_rate = 0.01  # 1% of vehicle value
    age_penalty = 0.0

    if q.age < 25:
        age_penalty = 0.005
    elif q.age > 70:
        age_penalty = 0.007

    coverage_multiplier = 1.0 if q.coverage_type == "basic" else 1.5

    premium = q.vehicle_value * (base_rate + age_penalty) * coverage_multiplier
    return {"premium": round(premium, 2), "currency": "USD"}
