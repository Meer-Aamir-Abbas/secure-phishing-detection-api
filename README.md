# Secure Phishing Detection API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Pytest](https://img.shields.io/badge/Tests-Pytest-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-black)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

A secure AI-powered phishing detection API built with **FastAPI**, **scikit-learn**, **Docker**, **authentication**, **rate limiting**, **logging**, **testing**, **GitHub Actions CI**, and **Render deployment**.

## Live Demo

- **API Base URL:** `https://secure-phishing-detection-api.onrender.com`
- **Swagger Docs:** `https://secure-phishing-detection-api.onrender.com/docs`
- **Health Check:** `https://secure-phishing-detection-api.onrender.com/health`

---

## Overview

This project classifies whether a given email or message is **phishing** or **legitimate** using a machine learning model trained on phishing email text.

It was designed as a production-style secure AI service with:
- ML model serving
- API key authentication
- rate limiting
- request logging
- automated testing
- Docker containerization
- CI with GitHub Actions
- live cloud deployment on Render

---

## Features

- Phishing vs legitimate text classification
- FastAPI REST API
- API key authentication using `x-api-key`
- Rate limiting to reduce abuse
- Input cleaning and validation
- Request logging
- Automated tests with `pytest`
- Dockerized deployment
- GitHub Actions CI workflow
- Live public deployment on Render

---

## Tech Stack

- **Language:** Python
- **ML:** scikit-learn, pandas, joblib
- **API:** FastAPI, Uvicorn
- **Security / Backend:** python-dotenv, SlowAPI
- **Testing:** pytest, httpx
- **DevOps:** Docker, GitHub Actions
- **Deployment:** Render

---

## Project Structure

```text
secure-phishing-detection-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── assets/
│   ├── local-fastapi-server.png
│   ├── phishing-prediction.png
│   ├── pytest-passed.png
│   ├── rate-limiting.png
│   └── render-live-deployment.png
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── model_loader.py
│   ├── schemas.py
│   └── utils.py
├── model/
│   └── phishing_model.pkl
├── tests/
│   └── test_api.py
├── training/
│   ├── train_model.py
│   └── phishing_email.csv
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt

API Endpoints

GET /health
{
  "status": "ok"
}

POST /predict

Required header:
x-api-key: mysecret123

Sample Request 
{
  "text": "Dear Customer, We detected unusual activity on your bank account. Your access will be suspended within 24 hours unless you verify your identity immediately. Click the secure link below to confirm your details and restore access: http://secure-bank-verify-login.com"
}

Sample Request
{
  "input_text": "Dear Customer, We detected unusual activity on your bank account. Your access will be suspended within 24 hours unless you verify your identity immediately. Click the secure link below to confirm your details and restore access: http://secure-bank-verify-login.com",
  "prediction": "phishing",
  "confidence": 0.9983
}

Screenshots

Local FastAPI Server
Phishing Prediction Result
Rate Limiting Protection
Automated Test Results
Render Live Deployment

Local Setup
git clone https://github.com/Meer-Aamir-Abbas/secure-phishing-detection-api.git
cd secure-phishing-detection-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Running Tests
python -m pytest

Docker 
docker build -t phishing-api .
docker run -p 8000:8000 --env-file .env phishing-api

CI/CD

GitHub Actions automatically:
	•	installs dependencies
	•	creates a sample .env
	•	creates a sample training dataset
	•	trains the model
	•	runs tests


Deployment

This project is deployed on Render as a Docker-based web service.

Author

Meer Aamir Abbas