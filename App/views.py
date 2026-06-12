from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *
from .models import *
from django.contrib import messages

# Create your views here.
class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class LoginView(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
