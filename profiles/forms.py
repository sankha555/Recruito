from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import LoginForm

class RegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bits_id', 'name', 'birthday', 'sex', 'city', 'bio', 'image']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'bio', 'image']
