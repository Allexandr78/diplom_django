from django.urls import  path
from .views import recipe_list, recipe_detail, create_recipe, base

urlpatterns = [
    path('', base, name='base'),
    path('recipe/list', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('create/', create_recipe, name='create_recipe'),
]
