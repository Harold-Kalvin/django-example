from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class EmailUserAdmin(UserAdmin):
    """Custom "ModelAdmin" extending Django's default "UserAdmin".

    Uses "email" instead of "username" in the fieldset.
    """

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, EmailUserAdmin)
