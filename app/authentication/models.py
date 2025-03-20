import uuid
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def _generate_username() -> str:
    return uuid.uuid4().hex


class User(AbstractUser):
    """Custom User model extending Django's default model.

    - Makes "email" unique.
    - Uses "email" instead of "username" as the unique identifier.
    - Generates a random "username" if needed.
    """

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_("email address"), unique=True, db_index=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        db_index=True,
        default=_generate_username,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )

    # field used as the unique identifier (set to "username" by default)
    USERNAME_FIELD = "email"

    # Prompted fields when using "createsuperuser".
    # Should not contain the USERNAME_FIELD or "password" as they will always be prompted for.
    REQUIRED_FIELDS: ClassVar[list[str]] = ["username"]

    def __str__(self) -> str:
        return str(self.email)
