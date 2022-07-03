from http.client import ResponseNotReady
from .models import Menu_Item, User, Menu
from .serializers import MenuItemSerializer, MenuSerializer, UserSerializer, ItemSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


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
        # add menu
        menu_serializer=self.get_serializer(data=data)
        if menu_serializer.is_valid(raise_exception=True):
            menu_serializer.save()

        for menu_item in menu_items:
            # add item
            item = menu_item['item']
            item['user_id'] = data['user_id']
            item_serializer = ItemSerializer(data=item)
            if item_serializer.is_valid(raise_exception=True):
                item_serializer.save()
                # add menu_item
                menu_item['item_id'] = item_serializer.data['id']
                menu_item['menu_id']=menu_serializer.data['id']
                menu_item_serializer=MenuItemSerializer(data=menu_item)
                if menu_item_serializer.is_valid(raise_exception=True):
                    menu_item_serializer.save()
        # response = menu_serializer.data
        # response_menu_items= Menu_Item.objects.filter(menu_id=menu_serializer.data['id'])
        # response_menu_items=MenuItemSerializer(response_menu_items, many=True)
        # response['menu_items']=response_menu_items.data

        response = Menu.objects.get(id=menu_serializer.data['id'])
        response=MenuSerializer(response)
        print(response)
        # print(menu_item_serializer.data['id'])
        # response = Menu_Item.objects.get(id=menu_item_serializer.data['id'])
        # response=MenuItemSerializer(response)
        # return Response(response.data)
        return Response('done')


