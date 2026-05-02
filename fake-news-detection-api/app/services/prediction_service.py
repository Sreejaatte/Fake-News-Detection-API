from app.models.model_loader import load_model

model, vectorizer = load_model()

def predict_news(text: str):
    vect = vectorizer.transform([text])
    pred = model.predict(vect)[0]
    proba = max(model.predict_proba(vect)[0])
    return {
        "prediction": "Fake" if pred == 1 else "Real",
        "confidence": round(float(proba), 4)
    }
