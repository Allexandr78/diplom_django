"""Модуль моделей приложения user."""
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ''' Модель профиля '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/user', default='static/img/user/baseavatar.jpg')
    objects = models.Manager()

    def __str__(self):
        return self.user.username
