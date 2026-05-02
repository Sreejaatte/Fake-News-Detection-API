import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

DATA_PATH = "data/sample_data.csv"
MODEL_DIR = "app/models"

os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(MODEL_DIR, "fake_news_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("Model trained and saved.")
