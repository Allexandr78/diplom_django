from django.contrib import admin
from .models import Recipe  # Импортируй свою модель

admin.site.register(Recipe)  # Регистрируем модель в админке
