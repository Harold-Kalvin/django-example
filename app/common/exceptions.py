from dataclasses import dataclass

from common.enums import ErrorCode


@dataclass
class GenericAPIError(Exception):
    error_message: str
    error_code: ErrorCode
    http_code: int

    def __str__(self) -> str:
        return self.error_message
