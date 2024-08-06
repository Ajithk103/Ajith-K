from django import forms
from new_app.models import FoodName, FoodName


class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodName
        fields = "__all__"
