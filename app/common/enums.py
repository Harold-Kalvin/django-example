from enum import Enum


class ErrorCode(str, Enum):
    pass


class AuthErrorCode(ErrorCode):
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    INVALID_TOKEN = "INVALID_TOKEN"
