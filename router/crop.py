import os
import joblib
import pandas as pd
from fastapi import APIRouter
from fastapi import Header, HTTPException
from schemas import crop_detection

router = APIRouter()

model = joblib.load("Crop_Classification_Model.pkl")

API_KEY = os.getenv("API_KEY")

@router.post("/crop_detections")
def crop_detection(
    details: crop_detection,
    x_api_key: str = Header(...)
):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    data = details.model_dump()

    if all(value == 0 for value in data.values()):
        raise HTTPException(
            status_code=400,
            detail="Invalid Input"
        )

    sample = pd.DataFrame([data])

    prediction = model.predict(sample)

    return {"prediction": prediction[0]}