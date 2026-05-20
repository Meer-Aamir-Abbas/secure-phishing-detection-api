import os
import secrets
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

API_KEY = (os.getenv("API_KEY") or "").strip()
if not API_KEY:
    raise RuntimeError(
        "API_KEY is not set or is empty. Set API_KEY in your environment or "
        "in a .env file at the project root before starting the application."
    )

def _api_keys_equal(provided: str, expected: str) -> bool:
    try:
        return secrets.compare_digest(
            provided.encode("utf-8"),
            expected.encode("utf-8"),
        )
    except (ValueError, TypeError, AttributeError, UnicodeEncodeError):
        return False

def verify_api_key(x_api_key: str = Header(...)):
    if not _api_keys_equal(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")