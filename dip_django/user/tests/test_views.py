"""Тесты для представлений приложения user"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user.models import Profile


class UserViewsTest(TestCase):
    """Тесты для представлений user"""

    @classmethod
    def setUpTestData(cls):
        """Создаем тестового пользователя"""
        cls.user = User.objects.create_user(username="testuser", password="testpass")
        cls.profile = Profile.objects.get(user=cls.user)

    def test_user_login_get(self):
        """Тест GET-запроса на страницу логина"""
        response = self.client.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

def test_user_login_post_invalid(self):
    """Тест неуспешного входа с неверными данными"""
    response = self.client.post(reverse("user:login"), {"username": "wronguser", "password": "wrongpass"})
    print(response.content.decode())  
    self.assertContains(response, "Введите правильные имя пользователя и пароль.")


    def test_user_login_post_invalid(self):
        """Тест неуспешного входа с неверными данными"""
        response = self.client.post(reverse("user:login"), {"username": "wronguser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
        self.assertContains(response, "Please enter a correct username and password.")

    def test_user_registration_get(self):
        """Тест GET-запроса на страницу регистрации"""
        response = self.client.get(reverse("user:registration"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/registration.html")

    def test_user_registration_post_valid(self):
        """Тест успешной регистрации"""
        response = self.client.post(reverse("user:registration"), {
            "username": "newuser",
            "password1": "Testpass123!",
            "password2": "Testpass123!"
        })
        self.assertRedirects(response, reverse("user:profile"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_registration_post_invalid(self):
        """Тест неуспешной регистрации (пароли не совпадают)"""
        response = self.client.post(reverse("user:registration"), {
            "username": "invaliduser",
            "password1": "Testpass123!",
            "password2": "wrongpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/registration.html")
        self.assertContains(response, "The two password fields didn’t match.")

    def test_user_profile_get_authenticated(self):
        """Тест отображения профиля для аутентифицированного пользователя"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("user:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/profile.html")

    def test_user_profile_get_unauthenticated(self):
        """Тест редиректа неаутентифицированного пользователя"""
        response = self.client.get(reverse("user:profile"))
        self.assertRedirects(response, f"{reverse('user:login')}?next={reverse('user:profile')}")

    def test_user_logout(self):
        """Тест выхода пользователя"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("user:logout"))
        self.assertRedirects(response, reverse("home"))
