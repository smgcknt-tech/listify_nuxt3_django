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
class MenuItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField('get_item')
    class Meta:
        model = Menu_Item
        fields = '__all__'
    def get_item(self, menu_item):
        return ItemSerializer(menu_item.item_id).data
class MenuSerializer(serializers.ModelSerializer):
    menu_items= MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = '__all__'
    