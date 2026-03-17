import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app

load_dotenv()

client = TestClient(app)
API_KEY = os.getenv("API_KEY")

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_success():
    response = client.post(
        "/predict",
        json={"text": "Your account has been suspended. Click here immediately to verify your details."},
        headers={"x-api-key": API_KEY}
    )
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "confidence" in data
    assert data["prediction"] in ["phishing", "legitimate"]

def test_predict_missing_api_key():
    response = client.post(
        "/predict",
        json={"text": "Your account has been suspended. Click here immediately to verify your details."}
    )
    assert response.status_code in [401, 422]

def test_predict_empty_text():
    response = client.post(
        "/predict",
        json={"text": ""},
        headers={"x-api-key": API_KEY}
    )
    assert response.status_code == 400