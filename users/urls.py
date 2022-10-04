from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('login_page/', views.login_page),
    path('make_user/', views.make_user),
    path('profile_page/', views.profile_page),
]