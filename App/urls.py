from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register('registration', RegistrationView)
routers.register('login', LoginView)

urlpatterns = [
    path('', include(routers.urls))
]