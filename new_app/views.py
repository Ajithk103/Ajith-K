from django.shortcuts import render, redirect

from new_app.forms import FoodForm
from new_app.models import FoodName


# Create your views here.
def home(request):
    return render(request, 'views.html')


def index(request):
    return render(request, 'index.html')


def dash(request):
    return render(request, 'dash.html')


def food_name(request):
    form = FoodForm()
    if request.method == 'POST':
        data = FoodForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'food_name.html',{"form":form})

def viewfood(request):
    data = FoodName.objects.all()

    return render(request, 'food_name.data.html',{'data':data})

# Delete

def deletefood(request,id):
    data = FoodName.objects.get(id=id)
    data.delete()
    return redirect("viewfood")

# Update

def updatefood(request,id):
    data = FoodName.objects.get(id=id)
    form = FoodForm(instance=data)
    if request.method == 'POST':
        data = FoodForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect("viewfood")
    return render(request, 'Update.html', {"form": form})






