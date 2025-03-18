"""Тесты представлений приложения recipes"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, Step
from django.core.files.uploadedfile import SimpleUploadedFile

class RecipeViewsTest(TestCase):
    """Тесты представлений приложения recipes"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password123")

        
        self.recipe = Recipe.objects.create(
            title="Тестовый рецепт",
            description="Описание тестового рецепта",
            author=self.user,
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

        
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe, name="Соль", quantity=10, unit="г"
        )

        
        self.step = Step.objects.create(
            recipe=self.recipe, number=1, description="Шаг 1: тестовый шаг"
        )

    def test_recipes_view(self):
        """Тест отображения списка рецептов"""
        response = self.client.get(reverse("recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes.html")
        self.assertContains(response, "Тестовый рецепт")

    def test_dish_detail_view(self):
        """Тест отображения деталей рецепта"""
        response = self.client.get(reverse("dish_detail", args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/dish_detail.html")
        self.assertContains(response, "Тестовый рецепт")
        self.assertContains(response, "Соль")
        self.assertContains(response, "Шаг 1: тестовый шаг")

    def test_add_recipe_view_not_logged_in(self):
        """Проверяем, что неавторизованный пользователь не может добавить рецепт"""
        response = self.client.get(reverse("add_recipe"))
        self.assertEqual(response.status_code, 302)  

    def test_add_recipe_view_logged_in(self):
        """Проверяем добавление нового рецепта авторизованным пользователем"""
        self.client.login(username="testuser", password="password123")

        form_data = {
            "title": "Новый рецепт",
            "description": "Описание нового рецепта",
            "ingredient_name": ["Соль"],
            "ingredient_quantity": ["5"],
            "step_description": ["Перемешать"]
        }

        response = self.client.post(reverse("add_recipe"), form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Recipe.objects.filter(title="Новый рецепт").exists())
        self.assertTrue(Ingredient.objects.filter(name="Соль").exists())
        self.assertTrue(Step.objects.filter(description="Перемешать").exists())
