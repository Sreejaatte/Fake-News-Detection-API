from fastapi import FastAPI
from app.api.v1.routes import router as v1_router
from app.utils.logging import setup_logging
from app.middleware.error_handler import ErrorHandlerMiddleware
from app.middleware.request_logging import RequestLoggingMiddleware

setup_logging()

app = FastAPI(
    title="Fake News Detection API",
    version="1.0.0",
    description="Production-grade ML inference API with FastAPI",
)

app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(RequestLoggingMiddleware)

app.include_router(v1_router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}
