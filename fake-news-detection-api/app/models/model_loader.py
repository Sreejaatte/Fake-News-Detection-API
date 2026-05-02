import joblib
from functools import lru_cache
from app.core.config import settings

@lru_cache()
def load_model():
    model = joblib.load(settings.MODEL_PATH)
    vectorizer = joblib.load(settings.VECTORIZER_PATH)
    return model, vectorizer
