from django.urls import path
from .models import *
from . import views

urlpatterns=[
    path("", views.loginUser, name="loginUser"), 
    path("registerUser/", views.registerUser, name="register-User"),
    path("homepage", views.index, name="homepage"),

]