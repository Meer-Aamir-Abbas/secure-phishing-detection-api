from pathlib import Path

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("training/phishing_email.csv")

# Keep only needed columns
df = df[["text_combined", "label"]].dropna()

# Ensure correct data types
df["text_combined"] = df["text_combined"].astype(str)
df["label"] = df["label"].astype(int)

# Features and labels
X = df["text_combined"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build ML pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(X_train, y_train)

# Predict on test set
y_pred = pipeline.predict(X_test)

# Show evaluation
print(classification_report(y_test, y_pred))

# Save model
project_root = Path(__file__).resolve().parent.parent
model_path = project_root / "model" / "phishing_model.pkl"
model_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(pipeline, model_path)
print(f"Model saved successfully to {model_path}")