from ninja_extra import status

from common.enums import HttpErrorCode

HTTP_ERROR_CODE_MAPPING = {
    status.HTTP_400_BAD_REQUEST: HttpErrorCode.BAD_REQUEST,
    status.HTTP_404_NOT_FOUND: HttpErrorCode.NOT_FOUND,
    status.HTTP_429_TOO_MANY_REQUESTS: HttpErrorCode.TOO_MANY_REQUESTS,
}
