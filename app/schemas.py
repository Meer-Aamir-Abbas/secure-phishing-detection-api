from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    text: str = Field(..., max_length=100_000)