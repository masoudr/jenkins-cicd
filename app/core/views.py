from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


