"""Этот файл содержит все URL-адреса, связанные с приложением пользователя."""

from django.urls import path
from user import views



app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("restration/", views.user_registration, name="registration"),
    path("profile/", views.user_profile, name="profile"),
    path("logout/", views.user_logout, name="logout"),
]



