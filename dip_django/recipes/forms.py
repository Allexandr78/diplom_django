""" Файл форм для приложения recipes """

from django import forms
from .models import Recipe, Ingredient, Step


class RecipeForm(forms.ModelForm):
    """Форма для добавления рецепта"""

    class Meta:
        """Описание модели и полей для формы"""

        model = Recipe
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название блюда"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Описание"}
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class IngredientForm(forms.ModelForm):
    """Форма для добавления ингредиента"""

    class Meta:
        """Описание модели и полей для формы"""

        model = Ingredient
        fields = ["name", "quantity"]


class StepForm(forms.ModelForm):
    """Форма для добавления шага приготовления"""

    class Meta:
        """Описание модели и полей для формы"""

        model = Step
        fields = ["number", "description"]
