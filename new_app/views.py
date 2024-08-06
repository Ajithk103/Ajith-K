from django.shortcuts import render

from new_app.forms import FoodForm


# Create your views here.
def home(request):
    return render(request, 'views.html')


def index(request):
    return render(request, 'index.html')


def dash(request):
    return render(request, 'dash.html')


def food_name(request):
    form = FoodForm
    return render(request, 'food_name.html',{"form":form})
