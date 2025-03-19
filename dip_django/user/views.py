"""Модуль представлений приложения user."""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import user
from .forms import ProfileForm


def user_login(request):
    """Функция входа пользователя."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("user:profile")
    else:
        form = AuthenticationForm()

    context = {"title": "Вход", "form": form}
    return render(request, "user/login.html", context)


def user_registration(request):
    """Функция регистрации пользователя."""
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user:profile")
    else:
        form = UserCreationForm()

    context = {"title": "Регистрация", "form": form}
    return render(request, "user/registration.html", context)


@login_required
def user_profile(request):
    """Функция отображения профиля пользователя."""
    profile = request.user.profile  
    user = request.user  

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)  
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()  
            profile.save()  
            return redirect("user:profile")  
    else:
        form = ProfileForm(instance=profile, initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

    context = {"title": "Профиль", "form": form, "profile": profile}
    return render(request, "user/profile.html", context)


def user_logout(request):
    """Функция выхода пользователя."""
    logout(request)
    return redirect("home")
