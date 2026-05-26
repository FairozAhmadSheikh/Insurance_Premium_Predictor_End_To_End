from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted category",
        example="High"
    )

    confidence: float = Field(
        ...,
        description="The prediction confidence score (0 to 1)",
        example=0.84
    )

    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all classes",
        example={
            "Low": 0.01,
            "Medium": 0.15,
            "High": 0.84
        }
    )