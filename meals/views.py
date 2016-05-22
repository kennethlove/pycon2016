from django.shortcuts import render


from . import models


def debug_view(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'meals/debug.html', {'recipes': recipes})
