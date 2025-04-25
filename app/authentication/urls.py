from allauth.account import views as allauth_views  # type: ignore
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    # allauth views
    path("login/", allauth_views.LoginView.as_view(), name="account_login"),
    path("signup/", allauth_views.SignupView.as_view(), name="account_signup"),
    path("logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
    path(
        "verify-email/",
        allauth_views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    # local views
    path("profile/", TemplateView.as_view(template_name="account/profile.html")),
]
