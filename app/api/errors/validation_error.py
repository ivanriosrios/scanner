from typing import Callable

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception(
    request: Request, exc: RequestValidationError
) -> Callable:
    """
    Handle the 422 error
    """

    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"error": "bad request"}),)