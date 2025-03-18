"""Тесты представлений приложения меню"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from menu.models import MenuItem
from recipes.models import Recipe


class MenuViewTest(TestCase):
    """Тестирование представления меню"""

    def setUp(self):
        """Создание тестового пользователя и тестовых рецептов"""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        self.recipe1 = Recipe.objects.create(title="Рецепт 1", description="Описание 1")
        self.recipe2 = Recipe.objects.create(title="Рецепт 2", description="Описание 2")

    def test_menu_get(self):
        """Тест GET-запроса к странице меню"""
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/menu.html")
        self.assertIn("menu_by_day", response.context)

    def test_add_menu_item(self):
        """Тест добавления блюда в меню"""
        response = self.client.post(
            reverse("menu"),
            {"action": "add", "day": "Понедельник", "recipe_id": self.recipe1.id},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            MenuItem.objects.filter(user=self.user, day="Понедельник").exists()
        )

    def test_remove_menu_item(self):
        """Тест удаления блюда из меню"""
        MenuItem.objects.create(user=self.user, day="Понедельник", recipe=self.recipe1)

        response = self.client.post(
            reverse("menu"), {"action": "remove", "day": "Понедельник"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            MenuItem.objects.filter(user=self.user, day="Понедельник").exists()
        )

    def test_random_all(self):
        """Тест случайного заполнения меню"""
        response = self.client.post(reverse("menu"), {"action": "random_all"})
        self.assertEqual(response.status_code, 302)
        menu_items = MenuItem.objects.filter(user=self.user)
        self.assertEqual(menu_items.count(), 7)
