from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer, ProduceSerializer
from .models import CustomUser, Produce

class ObtainTokenPairWithLocView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RestrictedView(APIView):
    def get(self, request):
        return Response(data={'Hello':'World'}, status = status.HTTP_200_OK)


class UserList (generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProduceList (generics.ListCreateAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class ProduceDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer