# 🚀 Fake News Detection API (Production-Grade)

## Overview
Production-ready ML API for fake news detection using FastAPI, TF-IDF, and Logistic Regression.

## Features
- Modular clean architecture
- Logging (JSON structured)
- Exception handling middleware
- Request logging middleware
- Docker & Render ready

## API
POST /api/v1/predict

Request:
{
  "text": "Breaking news..."
}

Response:
{
  "prediction": "Fake",
  "confidence": 0.92
}

## Run Locally
uvicorn app.main:app --reload

## Docker
docker build -t fake-news .
docker run -p 10000:10000 fake-news

## Deploy (Render)
Use render.yaml and connect repo

## Architecture
Client → FastAPI → Service → Model → Response
