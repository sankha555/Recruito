from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Org, OrgMember
from profiles.models import Profile
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import LoginForm

class OrgRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrgUpdateForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = ['name', 'type', 'about', 'logo']

class MemberRegForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['designation']
