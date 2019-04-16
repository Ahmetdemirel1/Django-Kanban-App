from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from core.forms import *

import random


def get_random_color():
    letters = '0123456789abcdef'
    color = '#'
    for i in range(0, 6):
        color += random.choice(letters)

    return color


def home(request):
    card_form = KanbanCardForm(request.POST)
    if request.user.is_authenticated:
        current_user = request.user
        username = User.objects.get(username=current_user.username)
        user_icon_text = current_user.username[0].upper()
        user_icon_color = get_random_color()
        return render(request, 'kanban.html', {"username": username,
                                               "user_icon_text": user_icon_text,
                                               "user_icon_color": user_icon_color,
                                               "card_form":card_form})

    return render(request, 'kanban.html')


def register(request):
    form = PersonForm(request.POST)

    if request.method == 'GET':

        return render(request, 'registration.html', {"form": form})

    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST.get('username'))
            messages.error(request, "Kullanıcı adı daha önce alınmış. Lütfen yeni bir kullanıcı adı giriniz.")

            return HttpResponseRedirect(reverse('register'))

        except:
            if form.is_valid():
                user = User.objects.create(
                username =request.POST.get('username'),
                password =request.POST.get('password'),
                email =request.POST.get('email'))
                user.set_password(request.POST.get('password'))
                user.save()

        return HttpResponseRedirect(reverse('login'))



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