from fastapi import APIRouter
from app.schemas.request import NewsRequest
from app.schemas.response import PredictionResponse
from app.services.prediction_service import predict_news

router = APIRouter(prefix="/api/v1", tags=["Prediction"])

@router.post("/predict", response_model=PredictionResponse)
def predict(req: NewsRequest):
    return predict_news(req.text)
