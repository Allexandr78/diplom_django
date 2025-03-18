"""Модели приложения recipes"""

from django.db import models
from django.contrib.auth.models import User

UNIT_CONVERSIONS = {
    "г": 1,
    "кг": 1000,
    "мл": 1,
    "л": 1000,
    "ч. л.": {
        "соль": 5,
        "сахар": 5,
        "сода": 7,
        "перец молотый": 3,
        "мука": 3,
        "масло растительное": 4.6,
        "мед": 12,
        "сметана": 8,
        "вода": 5,
        "молоко": 5,
        "какао-порошок": 3,
        "сахарная пудра": 3,
        "дрожжи сухие": 3,
    },
    "ст. л.": {
        "соль": 25,
        "сахар": 20,
        "сода": 20,
        "перец молотый": 9,
        "мука": 9,
        "масло растительное": 14,
        "мед": 26,
        "сметана": 27,
        "вода": 15,
        "молоко": 15,
        "какао-порошок": 8,
        "сахарная пудра": 10,
        "дрожжи сухие": 9,
    },
    "стакан": {
        "вода": 200,
        "молоко": 206,
        "мука": 114,
        "сахар": 185,
        "масло растительное": 185,
        "сахарная пудра": 134,
        "сметана": 210,
        "какао-порошок": 98,
    },
}


class Recipe(models.Model):
    """Модель рецепта"""

    title: models.CharField = models.CharField(
        max_length=255, verbose_name="Название блюда"
    )
    description: models.TextField = models.TextField(null=True,
        blank=True, verbose_name="Описание"
    )
    image = models.ImageField( null=True,
        blank=True, upload_to="img/recipe", verbose_name="Изображение"
    )
    author: models.ForeignKey = models.ForeignKey(
        null=True,
        blank=True,
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор рецепта",
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )
    objects = models.Manager()

    def __str__(self):
        return str(self.title)

    class Meta:
        """Мета класс модели рецепта"""

        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Ingredient(models.Model):
    """Модель ингредиента"""

    recipe: models.ForeignKey = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name: models.CharField = models.CharField(max_length=255, verbose_name="Ингредиент")
    quantity: models.FloatField = models.FloatField(
        null=True, verbose_name="Количество"
    )
    unit: models.CharField = models.CharField(
        max_length=50, verbose_name="Единица измерения"
    )
    objects = models.Manager()

    @property
    def quantity_in_grams(self):
        """Пересчитывает количество в граммы, если возможно"""
        conversion = UNIT_CONVERSIONS.get(self.unit)
        if isinstance(conversion, dict):
            return self.quantity * conversion.get(
                self.name.lower(), 1
            )
        elif isinstance(conversion, (int, float)):
            return self.quantity * conversion
        return self.quantity

    def __str__(self):
        return f"{self.recipe} - {self.name}: {self.quantity} {self.unit} ({self.quantity_in_grams} г)"

    class Meta:
        """Мета класс модели ингредиента"""

        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Step(models.Model):
    """Модель шага приготовления"""

    recipe: models.ForeignKey = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="steps", verbose_name="Рецепт"
    )
    number: models.PositiveIntegerField = models.PositiveIntegerField(
        null=True, verbose_name="Шаг №"
    )
    description: models.TextField = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name="Описание шага"
    )
    objects = models.Manager()

    class Meta:
        """Мета класс модели шага приготовления"""

        verbose_name = "Шаг"
        verbose_name_plural = "Шаги"

        ordering = ["recipe", "number"]

    def __str__(self):
        description = self.description if self.description else ""
        return f"{self.recipe}: Шаг {self.number}: {str(description)[:30]}..."
