from django.shortcuts import render
from django.contrib import messages
import requests
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrgRegForm, OrgUpdateForm, MemberRegForm
from .models import Org, OrgMember

def register_new_org(request):
    if request.method == 'POST':
        form = OrgRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('create_org_profile', pk=request.user.org.id)
    else :
        form = RegForm()

    return render(request, 'orgs/register.html', {'form' : form})

@login_required
def create_org_profile(request, pk):

    if request.method == 'POST':
        form = OrgUpdateForm(request.POST, request.FILES, instance=request.user.org)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'{name} created successfully')
            return redirect('org_detail')
    else :
        form = OrgRegForm(instance=request.user.org)

    return render(request, 'orgs/org_profile.html', {'form' : form})

@login_required
def update_org(request, pk):

    org = get_object_or_404(Org, pk = pk)
    if request.method == 'POST':
        form = OrgUpdateForm(instance=org)

        if form.is_valid():
            form.save()

    else:
        form = OrgUpdateForm(instance=org)

    context = {
        'form' : form
    }
    return render(request, 'orgs/org_profile.html', context)

# Create your views here.
