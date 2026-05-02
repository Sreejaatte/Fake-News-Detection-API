import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logging import logger

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = (time.time() - start) * 1000
        logger.info(f"{request.method} {request.url.path} {response.status_code} {duration:.2f}ms")
        return response
