from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer, ProduceSerializer, NoteSerializer,SuggestionSerializer, SeasonLocationSerializer, ResourceSerializer, UserSerializer
from .models import CustomUser, Produce, Note, Suggestion, SeasonLocation, Resource

class ObtainTokenPairWithLocView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProduceList (generics.ListCreateAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class ProduceDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class NoteList (generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class SuggestionList (generics.ListCreateAPIView):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

class SuggestionDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer


class SeasonLocationList (generics.ListCreateAPIView):
    queryset = SeasonLocation.objects.all()
    serializer_class = SeasonLocationSerializer

class SeasonLocationDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = SeasonLocation.objects.all()
    serializer_class = SeasonLocationSerializer

class ResourceList (generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer