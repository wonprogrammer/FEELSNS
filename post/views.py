from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.shortcuts import render, redirect


def main_page(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'main_page.html', {'posts':posts})


def make_post(request):
    return render(request, 'make_post.html')

def create_post(request):
    user = request.user
    post = Post()
    post.title = request.POST.get('title')
    post.body = request.POST.get('body')
    post.pub_date = timezone.datetime.now()
    post.nickname = user
    post.save()
    return redirect('/detailed_post/' + str(post.id))


def detailed_post(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detailed_post.html', {'post': post_detail})

def new_post(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'make_post.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )


