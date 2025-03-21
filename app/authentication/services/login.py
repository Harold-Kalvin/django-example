from django.contrib.auth import authenticate
from django.http import HttpRequest
from ninja_jwt.tokens import RefreshToken

from authentication.schemas import LoginInputSchema, LoginOutputSchema, UserSchema
from common.exceptions import InvalidCredentialsError


def login(request: HttpRequest, input: LoginInputSchema) -> LoginOutputSchema:
    user = authenticate(request, **input.model_dump())
    if not user:
        raise InvalidCredentialsError

    refresh = RefreshToken.for_user(user)
    return LoginOutputSchema(
        access=str(refresh.access_token),  # type: ignore[attr-defined]
        refresh=str(refresh),
        user=UserSchema.from_orm(user),
    )
