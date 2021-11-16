from django.shortcuts import render
# import forms
from .forms import *

# Create your views here.
def index(request):
    return render(request, "app/index.html", {})


def registerUser(request):
    return render(request, "registration/register.html", {})


def loginUser(request):
    return render(request, "registration/login.html", {})

