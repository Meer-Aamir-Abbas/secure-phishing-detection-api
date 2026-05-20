from pathlib import Path

import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "model" / "phishing_model.pkl"


def load_model():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found. Expected file at: {MODEL_PATH.resolve()}"
        )
    return joblib.load(MODEL_PATH)
