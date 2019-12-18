from django.shortcuts import render
from django.contrib import messages
import requests
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudSearchForm, SearchForm
from .models import Search
from orgs.models import Org, OrgMember

exclude_words = ["is", "the", "from", "of", "an", "then", "them", "a"]
org_pool = Org.objects.all()
org_list = [None]

@login_required
def search_orgs(request):
    if request.method == "POST":
        form  = SearchForm(request.POST)
        keywords = form.cleaned_data['interests'].split(",")

        for org in org_pool:
            org_info = org.about.split()
            for key in keywords:
                if key in org_info:
                    org_list.add(org)

        return redirect('search_results')

    else :
         form = SearchForm()

    return render(request, 'main/search_orgs.html', {'form':form})


@login_required
def search_results(request):
    return render(request, 'main/search_results.html', {'org_list':org_list})

@login_required
def apply_or_disapply(request, pk):
    org_user = get_object_or_404(User, pk=pk)
    stud_user = request.user.profile

    if profile in org.applicants.all():
        org.applicants.remove(stud_user)
        profile.applied_orgs.remove(org)
    else
        org.applicants.add(stud_user)
        profile.applied_orgs.add(org)

    return redirect('org_detail', pk=org_user.org.id)

@login_required
def search_studs(request):
    org = get_object_or_404(User, pk=request.user.org.id)
    studs = Profile.objects.all()
    flag = 0

    if request.method == "POST":
        form = SearchForm(request.POST)
        stud_id = form.cleaned_data['bits_id']

        for stud in studs:
            if stud_id == stud.bits_id:
                flag = 1
                return render(request, "success_search.html", {'stud':stud, 'org':org})

        if flag == 0:
            return render(request, "failed_search.html", {'stud_id':stud_id})

    return render(request, "search_studs.html", {"form":form})


@login_required
def add_delete_member(request, pk):

    org_user = get_object_or_404(User, pk=request.user.id)
    new_stud = get_object_or_404(User, pk=pk)

    if new_stud in org.members.all():
        org.members.remove(new_stud)
        new_stud.member_orgs.remove(org_user)
        messages.success(request, f'{new_stud.profile.name} added successfully as a member to {org_user.org.name}')
    else:
        org.members.add(new_stud)
        new_stud.member_orgs.add(org_user)
        messages.success(request, f'{new_stud.profile.name} removed from {org_user.org.name}')

    return redirect('org_detail', pk=org_user.org.id)

@login_required
def org_detail(request, pk):

    org = get_object_or_404(Org, pk=pk)
    return render(request, 'org_detail.html', {'org':org})

# Create your views here.
