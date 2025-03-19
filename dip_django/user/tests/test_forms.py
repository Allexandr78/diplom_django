"""Тесты для формы ProfileForm"""
from django.test import TestCase
from user.forms import ProfileForm

class ProfileFormTest(TestCase):
    """Тесты для формы ProfileForm"""

    def test_profile_form_valid_data(self):
        """Форма должна быть валидной с корректными данными"""
        form = ProfileForm(
            data={
                "first_name": "Иван",
                "last_name": "Иванов",
                "email": "ivan@example.com",
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_missing_fields(self):
        """Форма должна быть невалидной без обязательных полей"""
        form = ProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors)
        self.assertIn("last_name", form.errors)
        self.assertIn("email", form.errors)

    def test_profile_form_invalid_email(self):
        """Форма должна быть невалидной при некорректном email"""
        form = ProfileForm(
            data={
                "first_name": "Иван",
                "last_name": "Иванов",
                "email": "неправильный-емейл",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
