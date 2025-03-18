"""Тесты для представлений приложения main"""

from django.test import TestCase
from django.urls import reverse


class MainViewsTest(TestCase):
    """Класс для тестирования представлений приложения main"""

    def test_home_view(self):
        """Проверяем, что главная страница загружается и содержит нужные данные"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
        self.assertContains(response, "Главная")
        self.assertContains(response, "Вам нужно накормить семью?")

    def test_about_view(self):
        """Проверяем, что страница 'О нас' загружается корректно"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/about.html")
        self.assertContains(response, "О нас")
        self.assertContains(response, "Добро пожаловать в Семейное меню!")
