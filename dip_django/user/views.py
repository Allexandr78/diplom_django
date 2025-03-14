"""Модуль представлений приложения user."""

from calendar import c
from django.shortcuts import render
from django.template import context


def login(request):
    """Функция отображения страницы входа пользователя."""
    context = {
        "title": "Вход",
        "content": "Для входа введите логин и пароль.",
    }
    return render(request, "user/login.html", context)


def registration(request):
    """Функция отображения страницы регистрации пользователя."""
    context = {
        "title": "Регистрация",
        "content": "Для регистрации введите логин, пароль и адрес электронной почты.",
    }
    return render(request, "user/registration.html", context)


def profile(request):
    """Функция отображения страницы профиля пользователя."""
    context = {
        "title": "Профиль",
        "content": "Для изменения данных введите новые значения.",
    }
    return render(request, "user/profile.html", context)


def logout(request):
    """Функция отображения страницы выхода пользователя."""
    context = {
        "title": "Выход",
        "content": "Для выхода нажмите кнопку «Выйти».",
    }
    return render(request, "user/logout.html", context)
