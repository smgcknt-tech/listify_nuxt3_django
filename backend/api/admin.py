from django.contrib import admin
from .models import Currency_Unit, User, Item, Measurement_Unit, Meal_Type, Menu, List, Meal_Plan, Meal, Menu_Item, List_Item
# Register your models here.
myModels = [Currency_Unit, User, Item, Measurement_Unit, Meal_Type, Menu, List, Meal_Plan, Meal, Menu_Item, List_Item]
admin.site.register(myModels)