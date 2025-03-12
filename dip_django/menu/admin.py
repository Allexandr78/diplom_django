""" Модуль администрирования приложения меню. """

from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Меню на неделю."""

    list_display = ("user", "day", "recipe")
    list_filter = ("user", "day")
    search_fields = ("user__username", "day", "recipe__title")
