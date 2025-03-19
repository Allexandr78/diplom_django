from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile


class ProfileModelTest(TestCase):
    """Тесты для модели Profile"""

    @classmethod
    def setUpTestData(cls):
        """Создаем тестовые данные один раз перед всеми тестами"""
        cls.user = User.objects.create_user(username="testuser", password="testpass")
        cls.profile = Profile.objects.get(user=cls.user)

    def test_profile_created(self):
        """Проверяем, что профиль создается корректно"""
        self.assertEqual(self.profile.user.username, "testuser")

    def test_str_representation(self):
        """Проверяем __str__ метод"""
        self.assertEqual(str(self.profile), "testuser")

    def test_update_profile(self):
        """Проверяем обновление профиля"""
        self.profile.first_name = "Александр"
        self.profile.last_name = "Петров"
        self.profile.email = "alex@example.com"
        self.profile.save()
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.first_name, "Александр")
        self.assertEqual(updated_profile.last_name, "Петров")
        self.assertEqual(updated_profile.email, "alex@example.com")
