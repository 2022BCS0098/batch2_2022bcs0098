from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "btach2_2022bcs0098 API Running"}

@app.post("/predict")
def predict(data: list):
    arr = np.array(data).reshape(1, -1)
    pred = model.predict(arr)[0]

    return {
        "batch": "btach2_2022bcs0098",
        "prediction": float(pred)
    }
