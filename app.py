from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
from schema.User_Input import UserInput
from model.predict import MODEL_VERSION,model,predict_output
import pandas as pd 


app=FastAPI()

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

    user_input ={
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    prediction = predict_output(user_input)

    return JSONResponse(
        status_code=200,
        content={
            "Prediction":prediction
        }
    )