from django.shortcuts import render, redirect
import users

# Create your views here.


def login_page(request):
    return render(request, 'login_page.html')


def make_user(request):
    return render(request, 'make_user.html')


def profile_page(request):
    return render(request, 'profile_page.html')
