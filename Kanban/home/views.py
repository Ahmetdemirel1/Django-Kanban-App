from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import *
# Create your views here.


def home(request):

    if request.user.is_authenticated:
        current_user = request.user
        username = User.objects.get(username=current_user.username)

        return render(request, 'kanban.html', {"username": username})

    return render(request, 'kanban.html')


def register(request):
    form = PersonForm(request.POST)
    if request.method == 'GET':
        return render(request, 'registration.html', {"form": form})
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create(
            username =request.POST.get('username'),
            password =request.POST.get('password'),
            email =request.POST.get('email'))
            user.set_password(request.POST.get('password'))
            user.save()

        return HttpResponseRedirect(reverse('home'))




def login(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                user = None
            if user == None:
                messages.error(request, "Sorry, that login was invalid. Please try again.")

                return HttpResponseRedirect(reverse('login'))
            user_authenticate = authenticate(username=username, password=password)
            if user_authenticate is not None:
                auth_login(request, user_authenticate)
                print(user_authenticate)
                return HttpResponseRedirect(reverse('home'))
            if user_authenticate is None:
                messages.error(request, "Sifre hatali")
                return HttpResponseRedirect(reverse('login'))
    return render(request, 'login.html', {"form": form})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))