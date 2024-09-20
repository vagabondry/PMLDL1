# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from feature import FeatureExtraction  
import pickle

with open("./model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class URLData(BaseModel):
    url: str 

@app.post("/predict")
def predict(data: URLData):
    feature_extractor = FeatureExtraction(data.url)
    features = feature_extractor.getFeaturesList()
    
    features = [features]
    
    prediction = model.predict(features)
    
    return {"prediction": int(prediction[0])}
