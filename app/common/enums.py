from enum import Enum


class ErrorCode(str, Enum):
    pass


class CommonErrorCode(ErrorCode):
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"


class HttpErrorCode(ErrorCode):
    BAD_REQUEST = "BAD_REQUEST"
    NOT_FOUND = "NOT_FOUND"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
