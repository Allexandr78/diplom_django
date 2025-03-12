''' Модуль представлений приложения menu. '''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .models import MenuItem
import random


@login_required
def menu(request):
    """Отображение меню на неделю с возможностью случайного заполнения."""
    week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    user_menu = {day: None for day in week_days}

    menu_items = MenuItem.objects.filter(user=request.user)
    for item in menu_items:
        user_menu[item.day] = item.recipe

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "random_all":  
            recipes = list(Recipe.objects.all())
            if recipes:
                random.shuffle(recipes)  
                for day in week_days:
                    recipe = recipes.pop() if recipes else random.choice(Recipe.objects.all())
                    MenuItem.objects.update_or_create(user=request.user, day=day, defaults={"recipe": recipe})

        elif action == "add":
            day = request.POST.get("day")
            recipe_id = request.POST.get("recipe_id")
            recipe = Recipe.objects.get(id=recipe_id)
            MenuItem.objects.update_or_create(user=request.user, day=day, defaults={"recipe": recipe})

        elif action == "remove":
            day = request.POST.get("day")
            MenuItem.objects.filter(user=request.user, day=day).delete()

        return redirect("menu")

    context = {
        "title": "Меню",
        "content": "Меню на неделю",
        "menu_by_day": user_menu,
        "all_recipes": Recipe.objects.all(),
    }
    return render(request, "menu/menu.html", context)