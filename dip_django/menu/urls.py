''' Этот файл, который будет отвечать за маршрутизацию нашего приложения.
    В нем мы будем указывать, какие URL-адреса будут доступны в нашем приложении.'''
from django.urls import  path

from .views import menu


urlpatterns = [
    path('', menu, name='menu'),
]
