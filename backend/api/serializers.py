from rest_framework import serializers
from .models import Currency_Unit, User, Item, Measurement_Unit, Meal_Type, Menu, List, Meal_Plan, Meal, Menu_Item, List_Item
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','currency_unit']
        extra_kwargs = {'password': {'write_only': True}}
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
class MenuSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Menu
        fields = '__all__'
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        fields = '__all__'