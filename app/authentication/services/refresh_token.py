from ninja_jwt.tokens import RefreshToken

from authentication.schemas import RefreshTokenOutputSchema


def refresh_token(token_value: str) -> RefreshTokenOutputSchema:
    refresh_token = RefreshToken(token_value)
    refresh_token.set_jti()
    refresh_token.set_exp()
    refresh_token.set_iat()
    result = {"refresh": str(refresh_token), "access": str(refresh_token.access_token)}
    return RefreshTokenOutputSchema(**result)
