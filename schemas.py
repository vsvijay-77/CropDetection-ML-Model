from pydantic import BaseModel

class crop_detection(BaseModel):
    N:float
    P:float
    K:float
    temperature:float
    humidity:float
    ph:float
    rainfall:float