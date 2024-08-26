#!/usr/bin/env python3
""" Main function """

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.errors.validation_error import validation_exception
from app.api.routes.router import api_router
from app.config import settings


def get_application() -> FastAPI:
    """
    The main function that the function call

    Return: The model of fastApi
    """

    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
    )

    application.add_middleware(CORSMiddleware, allow_origins=["*"])

    # For add the validation of the 422 bad request
    application.add_exception_handler(RequestValidationError, validation_exception)

    application.include_router(api_router)

    return application


app = get_application()
