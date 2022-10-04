from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def make_post(request):
    return render(request, 'make_post.html')
