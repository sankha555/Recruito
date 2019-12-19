from django.contrib import admin
from django.urls import path
from .views import register, create_profile, update_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('create_profile/', create_profile, name='create_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='profile_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
]
