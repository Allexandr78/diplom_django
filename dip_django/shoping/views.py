"""Модуль для формирования списка покупок на основе меню."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from menu.models import MenuItem


UNIT_CONVERSION = {
    "г": 1,
    "кг": 1000,
    "мл": 1,
    "л": 1000,
    "ч. л.": {
        "соль": 5,
        "сахар": 5,
        "сода": 7,
        "перец молотый": 3,
        "мука": 3,
        "масло растительное": 4.6,
        "мед": 12,
        "сметана": 8,
        "вода": 5,
        "молоко": 5,
        "какао-порошок": 3,
        "сахарная пудра": 3,
        "дрожжи сухие": 3,
    },
    "ст. л.": {
        "соль": 25,
        "сахар": 20,
        "сода": 20,
        "перец молотый": 9,
        "мука": 9,
        "масло растительное": 14,
        "мед": 26,
        "сметана": 27,
        "вода": 15,
        "молоко": 15,
        "какао-порошок": 8,
        "сахарная пудра": 10,
        "дрожжи сухие": 9,
    },
    "стакан": {
        "вода": 200,
        "молоко": 206,
        "мука": 114,
        "сахар": 185,
        "масло растительное": 185,
        "сахарная пудра": 134,
        "сметана": 210,
        "какао-порошок": 98,
    },
}


@login_required
def generate_shopping_list(request):
    """Создает список покупок, объединяя одинаковые ингредиенты."""
    shopping_list = []

    menu_items = MenuItem.objects.filter(user=request.user)

    ingredient_dict = defaultdict(lambda: {"quantity": 0.0, "unit": "г."})

    for item in menu_items:
        for ingredient in item.recipe.ingredients.all():
            key = ingredient.name.lower().strip()
            unit = ingredient.unit.strip()

            try:
                quantity = float(str(ingredient.quantity_in_grams).replace(",", "."))
            except ValueError:
                quantity = 0.0

            if unit in UNIT_CONVERSION and unit != "г":
                conversion = UNIT_CONVERSION[unit]
                if isinstance(conversion, dict) and key in conversion:
                    quantity = conversion[key]
                elif isinstance(conversion, (int, float)):
                    quantity *= conversion
                unit = "г"

            ingredient_dict[key]["quantity"] += quantity
            ingredient_dict[key]["unit"] = unit

    shopping_list = [
        {"name": name, "quantity": round(data["quantity"]), "unit": data["unit"]}
        for name, data in ingredient_dict.items()
    ]

    context = {
        "title": "Список покупок",
        "content": "Список покупок на основе меню",
        "shopping_list": shopping_list,
    }

    return render(request, "shoping/shopping_list.html", context)
