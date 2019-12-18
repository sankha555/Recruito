from django.contrib import admin
from django.urls import path
from .views import search_orgs, search_studs, search_results, add_delete_member, apply_or_disapply, org_detail, stud_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('org_detail/<int:pk>/', org_detail, name='org_detail'),
    path('stud_detail/<int:pk>/', stud_detail, name='stud_detail'),
    path('search_orgs/', search_orgs, name='search_orgs'),
    path('search_studs/', search_studs, name='search_studs'),
    path('search_results/', search_results, name='search_results'),
    path('add_delete_member/<int:pk>/', add_delete_member, name='add_delete_member'),
    path('apply_or_disapply/<int:pk>/', apply_or_disapply, name='apply_or_disapply'),
    path('view_applications/', view_applications, name='view_applications'),
    path('reject_application/<int:pk>/', reject_application, name='reject_application'),
]
