''' Этот файл содержит все URL-адреса, связанные с приложением пользователя. '''
from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("restration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
