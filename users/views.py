from django.shortcuts import render, redirect
import users

# Create your views here.


def login_page(request):
    return render(request, 'login_page.html')