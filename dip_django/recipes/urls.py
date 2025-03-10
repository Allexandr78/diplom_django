''' Этот файл, который будет отвечать за маршрутизацию нашего приложения.
    В нем мы будем указывать, какие URL-адреса будут доступны в нашем приложении.'''
from django.urls import  path

from .views import recipe_list, recipe_detail, create_recipe, recipes

urlpatterns = [
    path('recipes', recipes, name='recipes'),
    path('recipe/list', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('create/', create_recipe, name='create_recipe'),
]
