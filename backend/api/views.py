from .models import User, Menu
from .serializers import MenuSerializer, UserSerializer
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


