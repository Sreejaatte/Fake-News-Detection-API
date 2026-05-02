from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.exceptions import AppError
from app.utils.logging import logger

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except AppError as ae:
            logger.error(f"AppError: {ae.message}")
            return JSONResponse(status_code=ae.status_code, content={"detail": ae.message})
        except Exception as e:
            logger.exception("Unhandled exception")
            return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
