import joblib

def load_model():
    return joblib.load("model/phishing_model.pkl")