""" Модель для списка покупок """

from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    """Модель для списка покупок"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    ingredient = models.CharField(max_length=255, verbose_name="Ингредиент")
    quantity = models.CharField(max_length=100, verbose_name="Количество")
    objects = models.Manager()

    def __str__(self):
        return f"{self.ingredient} - {self.quantity}"
