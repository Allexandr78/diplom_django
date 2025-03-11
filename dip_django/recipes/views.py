""" Этот файл содержит представления для приложения recipes. """

from .models import Ingredient, Recipe, Step
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def recipes(request):
    """Представление для отображения всех рецептов."""
    recipes = Recipe.objects.all()

    recipes_context = {
        "title": "Рецепты",
        "content": "Список рецептов",
        "recipes": recipes,
    }
    return render(
        request,
        "recipes/recipes.html",
        recipes_context,
    )


def dish_detail(request, id):
    """Представление для отображения деталей рецепта."""
    dish = get_object_or_404(Recipe, id=id)
    steps = dish.steps.all()
    ingredients = dish.ingredients.all()

    context = {
        "title": "Детали блюда",
        "content": "Пошаговый рецепт:",
        "dish": dish,
        "ingredients": ingredients,
        "steps": steps,
    }
    return render(request, "recipes/dish_detail.html", context)


@login_required
def add_recipe(request):
    """Представление для добавления нового рецепта."""
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)  
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            
            ingredient_names = request.POST.getlist("ingredient_name")
            ingredient_quantities = request.POST.getlist("ingredient_quantity")
            step_descriptions = request.POST.getlist("step_description")

            for name, quantity in zip(ingredient_names, ingredient_quantities):
                if name.strip():  
                    Ingredient.objects.create(recipe=recipe, name=name, quantity=quantity)

            for index, description in enumerate(step_descriptions, start=1):
                if description.strip():
                    Step.objects.create(recipe=recipe, number=index, description=description)

            return redirect("recipes")  

    else:
        recipe_form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"recipe_form": recipe_form})
   