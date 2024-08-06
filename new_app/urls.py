from django.urls import path

from new_app import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("index",views.index,name="index"),
    path("dash",views.dash,name="dash"),
    path("food_name",views.food_name,name="food_name")
]

