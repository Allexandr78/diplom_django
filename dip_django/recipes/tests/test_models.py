"""Тесты для моделей приложения recipes"""
from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, Step


class RecipeModelTest(TestCase):
    """Тесты для модели Recipe"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser")
        cls.recipe = Recipe.objects.create(
            title="Тестовый рецепт", description="Описание тестового рецепта", author=cls.user
        )

    def test_recipe_fields(self):
        """Тест полей модели Recipe"""
        recipe = self.recipe
        self.assertEqual(recipe.title, "Тестовый рецепт")
        self.assertEqual(recipe.description, "Описание тестового рецепта")
        self.assertEqual(recipe.author, self.user)

    def test_recipe_str(self):
        """Тест строкового представления модели Recipe"""
        self.assertEqual(str(self.recipe), "Тестовый рецепт")


class IngredientModelTest(TestCase):
    """Тесты для модели Ingredient"""

    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(title="Рецепт с ингредиентом")
        cls.ingredient = Ingredient.objects.create(
            recipe=cls.recipe, name="Мука", quantity=100, unit="г"
        )

    def test_ingredient_fields(self):
        """Тест полей модели Ingredient"""
        ingredient = self.ingredient
        self.assertEqual(ingredient.recipe, self.recipe)
        self.assertEqual(ingredient.name, "Мука")
        self.assertEqual(ingredient.quantity, 100)
        self.assertEqual(ingredient.unit, "г")

    def test_ingredient_str(self):
        """Тест строкового представления модели Ingredient"""
        expected_str = "Рецепт с ингредиентом - Мука: 100 г (100 г)"
        self.assertEqual(str(self.ingredient), expected_str)


class StepModelTest(TestCase):
    """Тесты для модели Step"""

    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(title="Рецепт с шагами")
        cls.step = Step.objects.create(
            recipe=cls.recipe, number=1, description="Первый шаг приготовления"
        )

    def test_step_fields(self):
        """Тест полей модели Step"""
        step = self.step
        self.assertEqual(step.recipe, self.recipe)
        self.assertEqual(step.number, 1)
        self.assertEqual(step.description, "Первый шаг приготовления")

    def test_step_str(self):
        """Тест строкового представления модели Step"""
        expected_str = "Рецепт с шагами: Шаг 1: Первый шаг приготовления..."
        self.assertEqual(str(self.step), expected_str)
