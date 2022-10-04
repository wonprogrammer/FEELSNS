from django.urls import path
from post import views


app_name = 'post'
urlpatterns = [
    path('main_page/', views.main_page),
    path('make_post/', views.make_post),
]