from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    path('login_page/', views.login_view, name='login_page'),
    path('make_user/', views.make_user, name='make_user'),
    path('logout/', views.logout, name='logout'),
    path('profile_page/', views.user_view, name='profile_page'),
    path('user/follow/<int:id>/', views.user_follow, name='user-follow'),
    path('fileupload/', views.fileUpload, name='fileupload'),
]