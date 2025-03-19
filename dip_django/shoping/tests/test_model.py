"""Тесты для модели ShoppingList"""

from django.test import TestCase
from django.contrib.auth.models import User
from shoping.models import ShoppingList


class ShoppingListModelTest(TestCase):
    """Тесты для модели ShoppingList"""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.shopping_item = ShoppingList.objects.create(
            user=self.user, ingredient="Мука", quantity="500 г"
        )

    def test_shopping_list_creation(self):
        """Проверяем, что объект создаётся корректно"""
        self.assertEqual(self.shopping_item.ingredient, "Мука")
        self.assertEqual(self.shopping_item.quantity, "500 г")
        self.assertEqual(self.shopping_item.user.username, "testuser")

    def test_shopping_list_str(self):
        """Проверяем метод __str__"""
        self.assertEqual(str(self.shopping_item), "Мука - 500 г")

    def test_shopping_list_user_relation(self):
        """Проверяем связь с пользователем"""
        self.assertEqual(self.shopping_item.user, self.user)
