from django.shortcuts import render
from django.contrib import messages
import requests
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, StudSearchForm
from .models import SearchForm
from orgs.models import Org, OrgMember
import smtplib

exclude_words = ["is", "the", "from", "of", "an", "then", "them", "a"]
org_pool = Org.objects.all()
org_list = [None]

def about(request):
    return render(request, "main/about.html")

@login_required
def home(request):
    user = request.user
    if user.profile.qualifier == 1:
        return redirect('stud_detail', pk = user.profile.id)
    elif user.org.qualifier == 1:
        return redirect('org_detail', pk = user.org.id)

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
    else:
        org.applicants.add(stud_user)
        profile.applied_orgs.add(org)

        #sending mail to organization
        mail = smtplib.SMTP('smtp.gmail.com', settings.EMAIL_PORT)
        mail.ehlo()
        mail.starttls()

        message = f'New Application:\nName: {stud_user.profile.name}\nID: {stud_user.profile.bits_id} \nEmail: {stud_user.profile.name}\n'

        mail.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        email = org_user.email

        try:
            mail.sendmail(settings.EMAIL_HOST_USER, email, message)
        except:
            pass

        mail.close()
        #mail closed

    return redirect('org_detail', pk=org_user.org.id)

@login_required
def search_studs(request):
    studs = Profile.objects.all()
    flag = 0

    if request.method == "POST":
        form = StudSearchForm(request.POST)
        stud_id = form.cleaned_data['bits_id']

        for stud in studs:
            if stud_id == stud.bits_id:
                flag = 1
                return render(request, "success_search.html", {'stud':stud, 'org':org})

        if flag == 0:
            return render(request, "failed_search.html", {'stud_id':stud_id})

    return render(request, "search_studs.html", {"form":form})

@login_required
def view_applications(request):

    org_user = get_object_or_404(User, pk=request.user.id)
    applicants = org_user.org.applicants.all()
    new_applicants = [None]

    for stud in applicants:
        if stud in org.members.all():
            pass
        else:
            new_applicants.add(stud)

    return render(request, "view_applications.html", {'new_applicants':new_applicants})

@login_required
def add_delete_member(request, pk):

    org_user = get_object_or_404(User, pk=request.user.id)
    new_stud = get_object_or_404(User, pk=pk)

    if new_stud in org.members.all():
        org_user.org.members.remove(new_stud)
        new_stud.profile.member_orgs.remove(org_user)
        messages.success(request, f'{new_stud.profile.name} added successfully as a member to {org_user.org.name}')
    else:
        org_user.org.members.add(new_stud)
        new_stud.profile.member_orgs.add(org_user)
        messages.success(request, f'{new_stud.profile.name} removed from {org_user.org.name}')

        #sending mail to student
        mail = smtplib.SMTP('smtp.gmail.com', settings.EMAIL_PORT)
        mail.ehlo()
        mail.starttls()

        message = f'Application Acceptance:\nName: {stud_user.profile.name}\nID: {stud_user.profile.bits_id}\nYou have been successfully inducted into {org_user.org.name}!'

        mail.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        email = new_stud.email

        try:
            mail.sendmail(settings.EMAIL_HOST_USER, email, message)
        except:
            pass

        mail.close()
        #mail closed

    return redirect('org_detail', pk=org_user.org.id)

@login_required
def reject_application(request, pk):

    org_user = get_object_or_404(User, pk=request.user.id)
    stud = get_object_or_404(User, pk=pk)

    if stud in org_user.org.applicants.all():
        applicants = org_user.org.applicants.all()
        new_applicants = applicants.remove(stud)
        messages.success(request, 'Application Rejected')

    return render(request, "view_applications.html", {'new_applicants':new_applicants, 'messages':messages})

@login_required
def org_detail(request, pk):

    org = get_object_or_404(Org, pk=pk)
    return render(request, 'org_detail.html', {'org':org})

@login_required
def stud_detail(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'stud_detail.html', {'profile':profile})

# Create your views here.
