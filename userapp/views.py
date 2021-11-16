from django.shortcuts import render, redirect
# import forms
from .forms import *

# Create your views here.
def index(request):
    title = "Homepage"
    return render(request, "app/index.html", {title: title})


def registerUser(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm[request.POST]

        if form.is_valid():
            form.save()

            return redirect('loginUser')
    title="Create a New User"
    return render(request, "registration/register.html", {"title":title, "form":form})


def loginUser(request):
    title="Login User"
    return render(request, "registration/login.html", {"title":title})

