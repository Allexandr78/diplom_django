"""Этот файл содержит URL-шаблоны для приложения main."""

from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
