from django.shortcuts import render, redirect
# import forms
from .forms import *
# import django authenticate method
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    title = "Homepage"
    return render(request, "app/index.html", {title: title})


def registerUser(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('loginUser')
    else:
        form=RegisterForm()

    title="Create a New User"
    return render(request, "registration/register.html", {"title":title, "form":form})


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password:
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('homepage')

            else:
                messages.error(request, "Username or password is Incorrect")

        else:
            messages.error(request, "Fill out all the fields")
    title="Login User"
    return render(request, "registration/login.html", {"title":title})


def logoutUser(request):
    logout(request)
    return redirect('loginUser')

