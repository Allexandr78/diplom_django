""" Этот файл содержит настройки административного интерфейса для приложения recipes. """

from django.contrib import admin
from .models import Recipe, Ingredient, Step


class IngredientInline(admin.TabularInline):
    """Встраивание ингредиентов в административный интерфейс рецепта."""

    model = Ingredient
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    """Настройки административного интерфейса для модели Ingredient."""

    list_display = ("recipe", "name", "quantity", "unit")
    list_filter = ("recipe",)
    search_fields = ("name", "recipe__name")
    ordering = ("recipe", "name")

    fields = ("recipe", "name", "quantity", "unit")


class StepInline(admin.TabularInline):
    """Встраивание шагов приготовления в административный интерфейс рецепта."""

    model = Step
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    """Настройки административного интерфейса для модели Recipe."""

    inlines = [IngredientInline, StepInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Step)
