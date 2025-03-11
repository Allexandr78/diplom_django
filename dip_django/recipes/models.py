from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(blank=True, upload_to='static/img/carusel/', verbose_name="Изображение")
    author = models.ForeignKey(
        null=True,
        blank=True,
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор рецепта",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name = models.CharField(max_length=255, verbose_name="Ингредиент")
    quantity = models.CharField(null=True, max_length=100, verbose_name="Количество")
    objects = models.Manager()

    def __str__(self):
        return f"{self.recipe}-{self.name}-{self.quantity}"


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="steps", verbose_name="Рецепт"
    )
    number = models.PositiveIntegerField(null=True, verbose_name="Шаг №")
    description = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name="Описание шага"
    )
    objects = models.Manager()

    class Meta:
        ordering = ["recipe", "number"]


    def __str__(self):
        description = self.description if self.description else ""
        return f"{self.recipe}: Шаг {self.number}: {description[:30]}..."
