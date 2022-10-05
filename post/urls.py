
from django.urls import path
from post import views


app_name = 'post'
urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('detailed_post/<int:post_id>', views.detailed_post, name='detailed_post'),
    path('make_post/', views.make_post, name='make_post'),
    path('create_post/', views.create_post, name='create_post'),
]