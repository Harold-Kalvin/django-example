from django.http import HttpRequest
from ninja import Router

from authentication.schemas import (
    LoginInputSchema,
    LoginOutputSchema,
    RefreshTokenInputSchema,
    RefreshTokenOutputSchema,
)
from authentication.services.login import login
from authentication.services.refresh_token import refresh_token

router = Router()


@router.post("/login")
def post_login(request: HttpRequest, input: LoginInputSchema) -> LoginOutputSchema:
    return login(request, input)


@router.post("/refresh")
def post_refresh(request: HttpRequest, input: RefreshTokenInputSchema) -> RefreshTokenOutputSchema:
    return refresh_token(input.refresh)
