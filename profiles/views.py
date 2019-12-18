from django.shortcuts import render
from django.contrib import messages
import requests
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegForm, UserUpdateForm, ProfileUpdateForm, ProfileCreateForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect('create_profile', pk=new_user.id)
    else :
        form = RegForm()

    return render(request, 'profiles/register.html', {'form' : form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        p_form = ProfileCreateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()

    else:
        p_form = ProfileCreateForm(instance=request.user.profile)

    context = {
        'p_form' : p_form
    }
    return render(request, 'profiles/create_profile.html', context)

@login_required
def update_profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'profiles/update_profile.html', context)



# Create your views here.
