from django.contrib.auth.models import User
from django.db import models

MEASUREMENTS = (
    ('tsp', 'teaspoon'),
    ('tbps', 'tablespoon'),
    ('c', 'cup'),
    ('gal', 'gallon'),
    ('quart', 'quart'),
    ('pint', 'pint'),
    ('g', 'gram'),
    ('mg', 'milligram'),
    ('kg', 'kilogram'),
    ('oz', 'ounce'),
    ('pinch', 'pinch'),
    ('pieces', 'pieces'),
)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep_time = models.IntegerField(help_text="in minutes")
    cook_time = models.IntegerField(help_text="in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Preparation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, related_name='recipies')
    preparation = models.ForeignKey(Preparation, related_name='+')
    quantity = models.DecimalField(decimal_places=3, max_digits=6)
    measurement = models.CharField(max_length=10, choices=MEASUREMENTS)

    class Meta:
        unique_together = ['recipe', 'ingredient', 'preparation']

    def __str__(self):
        return '{:.2f} {} {}, {}'.format(
            self.quantity,
            self.measurement,
            self.ingredient,
            self.preparation
        )


class UserMeal(models.Model):
    user = models.ForeignKey(User, related_name='meals')
    meal = models.ForeignKey(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)
