from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.core.validators import MinValueValidator
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types
# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id ) + '.' + self.name
    class Meta:
        abstract=True

class Currency_Unit(CommonInfo):
    # name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)

class User(AbstractBaseUser):
    username=models.CharField(max_length=50, unique=True)
    currency_unit=models.ForeignKey(Currency_Unit, on_delete=models.CASCADE, default=1)
    USERNAME_FIELD='username'

class Item(CommonInfo):
    # name=models.CharField(max_length=50)
    unit_price= models.PositiveSmallIntegerField(default=0,help_text='min value is 0')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Measurement_Unit(CommonInfo):
    # name=models.CharField(max_length=50)
    abbreviation=models.CharField(max_length=10)

class Meal_Type(CommonInfo):
    pass

class List(CommonInfo):
    # name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Menu(CommonInfo):
    # name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Meal_Plan(CommonInfo):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Meal(models.Model):
    date=models.DateField()
    meal_type=models.ForeignKey(Meal_Type, on_delete=models.CASCADE)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    meal_plan=models.ForeignKey(Meal_Plan, on_delete=models.CASCADE)

class Menu_Item(models.Model):
    menu_quantity=models.PositiveSmallIntegerField(default=0,help_text='min value is 0')
    measurement_unit=models.ForeignKey(Measurement_Unit, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)

class List_Item(models.Model):
    list_quantity=models.PositiveSmallIntegerField(default=0,help_text='min value is 0')
    list_note=models.CharField(max_length=200)
    purchased_flag=models.BooleanField(default=False)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    list=models.ForeignKey(List, on_delete=models.CASCADE)