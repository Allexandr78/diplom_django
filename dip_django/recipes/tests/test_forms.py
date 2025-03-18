"""Тесты для форм приложения recipes"""

from django.test import TestCase
from recipes.forms import RecipeForm, IngredientForm, StepForm
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


class RecipeFormTest(TestCase):
    """Тесты для формы RecipeForm"""

    def generate_image_file(self):
        """Генерирует тестовое изображение"""
        image = Image.new("RGB", (100, 100), color="red")  
        image_io = io.BytesIO()  
        image.save(image_io, format="JPEG")  
        image_io.seek(0)  
        return SimpleUploadedFile(
            "test_image.jpg", image_io.getvalue(), content_type="image/jpeg"
        )

    def test_recipe_form_valid_data(self):
        """Форма валидна с корректными данными"""
        image = self.generate_image_file()  
        form_data = {
            "title": "Тестовый рецепт",
            "description": "Описание тестового рецепта",
        }
        form = RecipeForm(data=form_data, files={"image": image})
        print("Form errors:", form.errors)  

    def test_recipe_form_invalid_data(self):
        """Форма невалидна без заголовка"""
        form = RecipeForm(data={"title": "", "description": "Описание"})
        self.assertFalse(form.is_valid())

    def test_recipe_form_widgets(self):
        """Проверка, что форма использует правильные widgets"""
        form = RecipeForm()
        self.assertEqual(form.fields["title"].widget.attrs["class"], "form-control")
        self.assertEqual(
            form.fields["description"].widget.attrs["class"], "form-control"
        )


class IngredientFormTest(TestCase):
    """Тесты для формы IngredientForm"""

    def test_ingredient_form_valid_data(self):
        """Форма валидна с корректными данными"""
        form = IngredientForm(data={"name": "Мука", "quantity": 100})
        self.assertTrue(form.is_valid())

    def test_ingredient_form_invalid_data(self):
        """Форма невалидна без названия ингредиента"""
        form = IngredientForm(data={"name": "", "quantity": 50})
        self.assertFalse(form.is_valid())


class StepFormTest(TestCase):
    """Тесты для формы StepForm"""

    def test_step_form_valid_data(self):
        """Форма валидна с корректными данными"""
        form = StepForm(data={"number": 1, "description": "Нарезать лук"})
        self.assertTrue(form.is_valid())

    def test_step_form_invalid_data(self):
        """Форма невалидна без номера шага"""
        form = StepForm(data={"number": "", "description": "Нарезать лук"})
        self.assertFalse(form.is_valid())
