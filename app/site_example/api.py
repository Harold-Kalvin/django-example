from django.http import Http404
from ninja import NinjaAPI
from ninja.errors import HttpError, ValidationError
from ninja_jwt.exceptions import TokenError

from common.exceptions import GenericAPIError
from site_example.exception_handlers import (
    generic_api_error_handler,
    ninja_http_error_handler,
    ninja_jwt_token_error_handler,
    ninja_validation_error_handler,
    not_found_error_handler,
    unexpected_error_handler,
)

api = NinjaAPI()
api.add_router("/auth/", "authentication.router.router")

api.add_exception_handler(Exception, unexpected_error_handler)
api.add_exception_handler(Http404, not_found_error_handler)
api.add_exception_handler(HttpError, ninja_http_error_handler)
api.add_exception_handler(ValidationError, ninja_validation_error_handler)
api.add_exception_handler(TokenError, ninja_jwt_token_error_handler)
api.add_exception_handler(GenericAPIError, generic_api_error_handler)
