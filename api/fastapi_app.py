import joblib
import pandas as pd
import json
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.pkl"
COLUMNS_PATH = BASE_DIR / "models" / "columns.json"

# Load model and training columns
model = joblib.load(MODEL_PATH)
with open(COLUMNS_PATH, "r") as f:
    model_columns = json.load(f)

# Pydantic schema = RAW inputs (not encoded)
class ClientData(BaseModel):
    age: int
    income: int
    tenure: int
    contract_type: str
    payment_method: str
    support_calls: int
    age_group: int

@app.post("/predict")
def predict(data: ClientData):
    # Convert input to DataFrame
    df = pd.DataFrame([data.dict()])

    # Encode incoming raw values
    df = pd.get_dummies(df)

    # Add missing columns
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns
    df = df[model_columns]

    # Predict
    prediction = int(model.predict(df)[0])

    return {"prediction": prediction}
