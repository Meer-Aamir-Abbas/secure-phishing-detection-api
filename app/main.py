from fastapi import FastAPI, HTTPException, Depends, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.schemas import PredictionRequest
from app.model_loader import load_model
from app.auth import verify_api_key
from app.utils import logger, clean_text

app = FastAPI(title="Secure Phishing Detection API")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

model = load_model()

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.post("/predict")
@limiter.limit("5/minute")
def predict(request: Request, payload: PredictionRequest, _: str = Depends(verify_api_key)):
    logger.info("Prediction request received")

    text = clean_text(payload.text)

    if not text:
        logger.warning("Empty input text received")
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    label_map = {
        0: "legitimate",
        1: "phishing"
    }

    readable_prediction = label_map.get(int(prediction), "unknown")

    logger.info(f"Prediction completed: {readable_prediction}")

    return {
        "input_text": text,
        "prediction": readable_prediction,
        "confidence": round(float(confidence), 4)
    }