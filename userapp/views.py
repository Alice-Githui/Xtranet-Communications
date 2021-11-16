from django.shortcuts import render
# import forms
from .forms import *

# Create your views here.
def index(request):
    title = "Homepage"
    return render(request, "app/index.html", {title: title})


def registerUser(request):
    title="Create a New User"
    return render(request, "registration/register.html", {"title":title})


def loginUser(request):
    title="Login User"
    return render(request, "registration/login.html", {"title":title})

