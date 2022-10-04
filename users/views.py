from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def profile_page(request):
    return render(request, 'profile_page.html')


def make_user(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
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


def login_view(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id', '')
        password = request.POST.get('password', '')
        me = auth.authenticate(request, login_id=login_id, password=password)
        #me = UserModel.object.get(username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/') # 글쓰기 페이지
        else:
            return render(request, 'login_page.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'login_page.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login_page')


@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(login_id=request.user.login_id)
        return render(request, 'user/profile_page.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/users')