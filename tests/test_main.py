import json

import pytest
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from Exceptions.generic_exception import GenericException
from Exceptions.not_found_exception import NotFoundException
from main import generic_exception_handler, validation_exception_handler, not_found_exception_handler


@pytest.mark.asyncio
async def test_validation_exception_handler():
    request = Request(scope={"type": "http"})
    exception = RequestValidationError("Generic test error message")
    response = await  validation_exception_handler(request, exception)
    json_response = json.loads(response.body)
    assert isinstance(response, JSONResponse)
    assert response.status_code == 403
    assert "error_message" in json_response, "'message' key is missing in the response"
    assert "errors" in json_response, "'message' key is missing in the response"


@pytest.mark.asyncio
async def test_generic_exception_handler():
    request = Request(scope={"type": "http"})
    exception = GenericException("Generic test error message")
    response = await  generic_exception_handler(request, exception)
    json_response = json.loads(response.body)
    assert response.status_code == 500
    assert isinstance(response, JSONResponse)
    assert "error_message" in json_response, "'message' key is missing in the response"


@pytest.mark.asyncio
async def test_not_found_exception_handler():
    request = Request(scope={"type": "http"})
    exception = NotFoundException("Not Found Exception Message")
    response = await  not_found_exception_handler(request, exception)
    json_response = json.loads(response.body)
    assert response.status_code == 404
    assert isinstance(response, JSONResponse)
    assert "error_message" in json_response, "'message' key is missing in the response"

