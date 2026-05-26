from fastapi import FastAPI,Path,HTTPException

import pickle
from fastapi.responses import JSONResponse
import pandas as pd
from schema.User_Input import UserInput

MODEL_VERSION="1.0.0"

app=FastAPI()

# Load Model first
with open('model/Model.pkl','rb')as f:
    model=pickle.load(f)

# Home Route 
@app.get('/')
def home():
    return JSONResponse(status_code=200,content={"message":"This is a Insurance prediction API 💖"})

# Health check route for Cloud Platform Deployment
@app.post('/health')
def health_check():
    return {"status":'OK',
            'Model_Version':MODEL_VERSION,
            'Loaded_Model':model is not None
            }

@app.post('/predict')
def predict_premium(data: UserInput):

    input_data = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    prediction = model.predict(input_data)

    return JSONResponse(
        status_code=200,
        content={
            "Prediction":prediction.tolist()
        }
    )