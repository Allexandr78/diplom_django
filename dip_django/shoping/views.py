""" Модуль для формирования списка покупок на основе меню. """

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from menu.models import MenuItem
from recipes.models import Ingredient
from shoping.models import ShoppingList


@login_required
def generate_shopping_list(request):
    """Формируем список покупок на основе меню."""
    user_menu = MenuItem.objects.filter(user=request.user)
    shopping_list = {}

    for item in user_menu:
        ingredients = Ingredient.objects.filter(recipe=item.recipe)
        for ingredient in ingredients:
            if ingredient.name in shopping_list:

                shopping_list[ingredient.name] += f", {ingredient.quantity}"
            else:
                shopping_list[ingredient.name] = ingredient.quantity

    ShoppingList.objects.filter(user=request.user).delete()
    for name, quantity in shopping_list.items():
        ShoppingList.objects.create(
            user=request.user, ingredient=name, quantity=quantity
        )

    context = {
        "title": "Список покупок",
        "content": "Список покупок на основе меню",
        "shopping_list": shopping_list,
    }

    return render(
        request,
        "shoping/shopping_list.html",
        context,
    )
