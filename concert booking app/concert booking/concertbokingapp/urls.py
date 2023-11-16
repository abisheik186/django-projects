from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from concertbokingapp import views as user_views

urlpatterns = [
    path('', user_views.home, name='home'),
    path('register/',user_views.register,name='register'),
    path('book/',user_views.booktickets,name='booktickets'),
    path('login/', auth_views.LoginView.as_view(template_name='home.html',next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html',next_page='home'), name='logout'),
]