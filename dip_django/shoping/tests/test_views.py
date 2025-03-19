"""Тесты представлений приложения shoping"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from menu.models import MenuItem
from recipes.models import Recipe, Ingredient


class ShoppingListViewTest(TestCase):
    """Тестирование представления списка покупок"""

    def setUp(self):
        """Создание тестового пользователя, рецептов и ингредиентов"""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        self.recipe1 = Recipe.objects.create(title="Рецепт 1", description="Описание 1")
        self.recipe2 = Recipe.objects.create(title="Рецепт 2", description="Описание 2")

        self.ingredient1 = Ingredient.objects.create(
            name="Мука", quantity=200, unit="г", recipe=self.recipe1
        )
        self.ingredient2 = Ingredient.objects.create(
            name="Сахар", quantity=100, unit="г", recipe=self.recipe1
        )
        self.ingredient3 = Ingredient.objects.create(
            name="Мука", quantity=1, unit="стакан", recipe=self.recipe2
        )

        MenuItem.objects.create(user=self.user, day="Понедельник", recipe=self.recipe1)
        MenuItem.objects.create(user=self.user, day="Вторник", recipe=self.recipe2)

    def test_shopping_list_view(self):
        """Тест загрузки страницы списка покупок"""
        response = self.client.get(reverse("shopping_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shoping/shopping_list.html")
        self.assertIn("shopping_list", response.context)

    def test_shopping_list_content(self):
        """Тест корректности списка покупок"""
        response = self.client.get(reverse("shopping_list"))
        shopping_list = response.context["shopping_list"]

        ingredients = {item["name"]: item["quantity"] for item in shopping_list}

        self.assertEqual(ingredients.get("мука"), 314)
        self.assertEqual(ingredients.get("сахар"), 100)
