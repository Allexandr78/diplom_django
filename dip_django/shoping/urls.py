"""В этом файле мы создаем пути для нашего приложения shoping"""

from django.urls import path

from shoping.views import generate_shopping_list


urlpatterns = [
    path("", generate_shopping_list, name="shopping_list"),
]
