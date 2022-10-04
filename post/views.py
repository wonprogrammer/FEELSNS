from django.shortcuts import render
from .models import Post

def main_page(request):
    return render(request, 'main_page.html')


def make_post(request):
    if request.method == 'GET': 
        user = request.user.is_authenticated 
        if user: 
            return render(request, 'post/detailed_post.html')
        else: 
            return redirect('/login_page')
    elif request.method == 'POST': 
        user = request.user 
        my_post = Post() 
        my_post.author = user 
        my_post.content = request.POST.get('my-post', '')
        my_post.save()
        return redirect('post/detailed_post.html')


def detailed_post(request):
    return render(request, 'post/detailed_post.html')
