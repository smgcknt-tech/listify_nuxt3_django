from http.client import ResponseNotReady

import django
from .models import Menu_Item, User, Menu
from .serializers import MenuItemSerializer, MenuSerializer, UserSerializer, ItemSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import *


# Create your views here.
class UserSignUp(generics.CreateAPIView) :
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserLogin(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }   
        return Response(content) 
class UserDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
class MenuCreate(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request):
        data = request.data
        menu_items = data['menu_items']
        try:
            # add menu
            menu_serializer=self.get_serializer(data=data)
            if menu_serializer.is_valid(raise_exception=True):
                menu_serializer.save()
            # add item
            items = [dict(menu_item['item'], **{'user_id':data['user_id']}) for menu_item in menu_items]
            item_serializer = ItemSerializer(data=items,many=True)
            if item_serializer.is_valid(raise_exception=True):
                item_serializer.save()
            # add menu_item
            menu_items = [dict(menu_item, menu_id=menu_serializer.data['id'], item_id=item_serializer.data[i]['id']) for i,menu_item in enumerate(menu_items)]
            menu_item_serializer=MenuItemSerializer(data=menu_items, many=True)
            if menu_item_serializer.is_valid(raise_exception=True):
                menu_item_serializer.save()

            response = Menu.objects.get(id=menu_serializer.data['id'])
            response=MenuSerializer(response)
            return Response(response.data)
        except Exception as e:
            raise APIException(e)


