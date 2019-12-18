from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Search
from profiles.models import Profile
from orgs.models import Org, OrgMember
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import LoginForm

class SearchForm(models.ModelForm):

    class Meta:
        model = SearchForm
        fields = ['type', 'interests']

class StudSearchForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bits_id']
