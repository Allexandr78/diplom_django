''' Модель меню '''
from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class MenuItem(models.Model):
    '''Модель меню'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(
        max_length=20,
        choices=[
            ("Понедельник", "Понедельник"),
            ("Вторник", "Вторник"),
            ("Среда", "Среда"),
            ("Четверг", "Четверг"),
            ("Пятница", "Пятница"),
            ("Суббота", "Суббота"),
            ("Воскресенье", "Воскресенье"),
        ],
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ''' Мета класс уникальность комбинации пользователя и дня '''
        unique_together = ("user", "day")

    def __str__(self):
        return f"{self.day}: {self.recipe.title}"
