from django.contrib import admin
from .models import Recipe, Ingredient, Step

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1 

class StepInline(admin.TabularInline):
    model = Step
    extra = 1  

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Step)
