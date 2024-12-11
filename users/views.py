from django.shortcuts import render

from users.forms import UserLoginForm

def login(request):
    form = UserLoginForm()
    context = {
        'title': 'Home - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Home - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Home - Кабинет'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...