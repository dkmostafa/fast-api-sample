from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from Exceptions.generic_exception import GenericException
from Exceptions.not_found_exception import NotFoundException
from modules.User.user_routes import user_router

app = FastAPI()

app.include_router(user_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=403,
        content={
            "error_message": "There was a validation error in your request.",
            "errors": exc.errors(),
        },
    )


@app.exception_handler(GenericException)
async def generic_exception_handler(request: Request, exc: GenericException):
    return JSONResponse(
        status_code=500,
        content={
            "error_message": exc.message,
        },
    )


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error_message": exc.message,
        },
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error_message": str(exc),
        },
    )


@app.get("/health")
def read_root():
    return {"hello world"}
