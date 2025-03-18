"""Тесты модели MenuItem"""
from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe
from menu.models import MenuItem


class MenuItemModelTest(TestCase):
    """Тесты модели MenuItem"""

    def setUp(self):
        """Подготовка данных"""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.recipe1 = Recipe.objects.create(title="Суп", description="Горячий суп")
        self.recipe2 = Recipe.objects.create(title="Салат", description="Легкий салат")

    def test_create_menu_item(self):
        """Тест создания объекта"""
        menu_item = MenuItem.objects.create(user=self.user, day="Понедельник", recipe=self.recipe1)
        self.assertEqual(MenuItem.objects.count(), 1)
        self.assertEqual(menu_item.user, self.user)
        self.assertEqual(menu_item.recipe, self.recipe1)
        self.assertEqual(menu_item.day, "Понедельник")

    def test_unique_together(self):
        """Тест уникальности (user, day, recipe)"""
        MenuItem.objects.create(user=self.user, day="Вторник", recipe=self.recipe1)

        MenuItem.objects.create(user=self.user, day="Вторник", recipe=self.recipe2)

        with self.assertRaises(Exception):
            MenuItem.objects.create(user=self.user, day="Вторник", recipe=self.recipe1)

    def test_str_representation(self):
        """Тест метода __str__"""
        menu_item = MenuItem.objects.create(user=self.user, day="Среда", recipe=self.recipe1)
        self.assertEqual(str(menu_item), "Среда: Суп")
