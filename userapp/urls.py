from django.urls import path
from .models import *
from . import views

urlpatterns=[
    path("homepage", views.index, name="homepage"),

]