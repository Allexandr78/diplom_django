from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Step
from .forms import RecipeForm, IngredientForm, StepForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def menu(request):
      return render(request, "recipes/menu.html")


def base(request):
    recipes = Recipe.objects.all()
    
    return render(request, "base.html", {"recipe": recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


@login_required
def add_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredients = request.POST.getlist("ingredient_name")
            amounts = request.POST.getlist("ingredient_amount")
            steps = request.POST.getlist("step_instruction")

            for name, amount in zip(ingredients, amounts):
                Ingredient.objects.create(recipe=recipe, name=name, amount=amount)

            for index, instruction in enumerate(steps, start=1):
                Step.objects.create(
                    recipe=recipe, step_number=index, instruction=instruction
                )

            return redirect("recipe_list")

    else:
        recipe_form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"recipe_form": recipe_form})


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


@login_required
def create_recipe(request):
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=3)
    StepFormSet = inlineformset_factory(Recipe, Step, form=StepForm, extra=3)

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)
        step_formset = StepFormSet(request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid() and step_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user  
            recipe.save()

            ingredient_formset.instance = recipe
            step_formset.instance = recipe
            ingredient_formset.save()
            step_formset.save()

            return redirect('recipe_list') 

    else:
        recipe_form = RecipeForm()
        ingredient_formset = IngredientFormSet()
        step_formset = StepFormSet()

    return render(request, 'recipes/recipe_form.html', {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
    })
