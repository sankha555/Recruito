from django.contrib import admin
from django.urls import path
from .views import register_new_org, create_org_profile, update_org
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_new_org, name='register'),
    path('create_org_profile/', create_org_profile, name='create_org_profile'),
    path('update_org/', update_org, name='update_org'),
    path('login/', auth_views.LoginView.as_view(template_name='orgs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='orgs/logout.html'), name='logout'),
]
