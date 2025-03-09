'''
    Файл views.py отвечает за отображение страниц сайта.
    В данном файле создаются функции, которые будут обрабатывать запросы к серверу.
    В данном случае, функция about отвечает за отображение страницы "О нас".
'''
from django.shortcuts import render

def home(request):
    '''
        Функция home отвечает за отображение главной страницы сайта.
        В данной функции создается словарь home_context, который содержит информацию о странице.
        Далее функция render возвращает страницу home.html, передавая в нее словарь home_context.
    '''
    home_context = {"title": "Главная", "content": "Добро пожаловать на главную страницу"}

    return render(request, "main/home.html", home_context)

def about(request):
    '''
        Функция about отвечает за отображение страницы "О нас".
        В данной функции создается словарь about_context, который содержит информацию о странице.
        Далее функция render возвращает страницу about.html, передавая в нее словарь about_context.
    '''
    about_context = {"title": "О нас", "content": "Добро пожаловать на страницу «О нас»"}

    return render(request, "main/about.html", about_context)
