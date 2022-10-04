from django.shortcuts import render, redirect
from .models import UserModel, ProfileModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login_page(request):
    return render(request, 'login_page.html')

def make_user(request):
    if request.method == 'GET':
        # user = request.user.is_authenticated
        # if user:
        #     return redirect('/')
        # else:
        return render(request, 'make_user.html')
    elif request.method == 'POST':
        login_id = request.POST.get('login_id', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')

        if password != password2:
            return render(request, 'make_user.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if login_id == '' or password == '':
                return render(request, 'make_user.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다!'})

            exist_user = UserModel.objects.filter(login_id=login_id)
            if exist_user:
                return render(request, 'make_user.html', {'error': '사용자가 존재합니다'})
            else:
                new_user = UserModel()
                new_user.login_id = login_id
                new_user.password = password
                new_user.nickname = nickname
                new_user.save()
                return redirect('/login_page')