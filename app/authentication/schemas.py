from ninja import Schema
from pydantic import EmailStr


class UserSchema(Schema):
    email: str
    username: str


class LoginOutputSchema(Schema):
    access: str
    refresh: str
    user: UserSchema


class LoginInputSchema(Schema):
    email: EmailStr
    password: str


class RefreshTokenInputSchema(Schema):
    refresh: str


class RefreshTokenOutputSchema(Schema):
    access: str
    refresh: str
