from dataclasses import dataclass

from ninja_extra import status

from common.enums import AuthErrorCode, ErrorCode


@dataclass
class GenericAPIError(Exception):
    error_message: str
    error_code: ErrorCode
    http_code: int

    def __str__(self) -> str:
        return self.error_message


@dataclass
class InvalidCredentialsError(GenericAPIError):
    error_message: str = "No active account found with the given credentials."
    error_code: ErrorCode = AuthErrorCode.INVALID_CREDENTIALS
    http_code: int = status.HTTP_401_UNAUTHORIZED
