import logging
from typing import TypedDict

from django.http import Http404, HttpRequest, JsonResponse
from ninja.errors import HttpError, ValidationError
from ninja_extra import status

from common.enums import CommonErrorCode, ErrorCode, HttpErrorCode
from common.exceptions import GenericAPIError
from common.mappings import HTTP_ERROR_CODE_MAPPING


class ErrorResponseDict(TypedDict):
    code: ErrorCode
    message: str
    details: list[dict[str, str]] | None


def _error_response(
    error_code: ErrorCode,
    error_message: str,
    http_code: int,
    details: list[dict[str, str]] | None = None,
) -> JsonResponse:
    response: ErrorResponseDict = {"code": error_code, "message": error_message, "details": details}
    return JsonResponse(response, status=http_code)


def unexpected_error_handler(
    request: HttpRequest, exc: Exception | type[Exception]
) -> JsonResponse:
    logging.exception(exc)
    return _error_response(
        error_code=CommonErrorCode.UNEXPECTED_ERROR,
        error_message="An unexpected error has occurred. Please contact an administrator.",
        http_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def not_found_error_handler(request: HttpRequest, exc: Http404 | type[Http404]) -> JsonResponse:
    return _error_response(
        error_code=HttpErrorCode.NOT_FOUND,
        error_message="Object not found.",
        http_code=status.HTTP_404_NOT_FOUND,
    )


def ninja_http_error_handler(
    request: HttpRequest, exc: HttpError | type[HttpError]
) -> JsonResponse:
    return _error_response(
        error_code=HTTP_ERROR_CODE_MAPPING.get(exc.status_code, CommonErrorCode.UNEXPECTED_ERROR),
        error_message=exc.message,
        http_code=exc.status_code,
    )


def ninja_validation_error_handler(
    request: HttpRequest, exc: ValidationError | type[ValidationError]
) -> JsonResponse:
    details = []
    message = "Please fix the following validation errors."
    for error in exc.errors:
        try:
            details.append({"field": error["loc"][2], "message": f"{error['msg']}."})
        except IndexError:
            message = "Please provide a body."
            break

    return _error_response(
        error_code=CommonErrorCode.VALIDATION_ERROR,
        error_message=message,
        http_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        details=details or None,
    )


def generic_api_error_handler(
    request: HttpRequest, exc: GenericAPIError | type[GenericAPIError]
) -> JsonResponse:
    return _error_response(
        error_code=exc.error_code, error_message=exc.error_message, http_code=exc.http_code
    )
