''' Этот файл, который будет отвечать за маршрутизацию нашего приложения.
    В нем мы будем указывать, какие URL-адреса будут доступны в нашем приложении.'''
from django.urls import  path

from .views import dish_detail, recipes, add_recipe

urlpatterns = [
    path('recipes', recipes, name='recipes'),
    path('dish/<int:id>/', dish_detail, name='dish_detail'),
    path('add/', add_recipe, name='add_recipe'),
]
