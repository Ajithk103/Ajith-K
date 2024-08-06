from django.db import models


# Create your models here.
class FoodName(models.Model):
    food_category = (
        ('veg', 'veg'),
        ('non', 'non veg')

    )
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=30, choices=food_category)
