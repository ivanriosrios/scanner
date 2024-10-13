from fastapi import APIRouter

from app.api.routes import data_scanner

api_router = APIRouter()
api_router.include_router(data_scanner.router, tags=["Input Data"])

