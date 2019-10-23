from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from .forms import SignUpForm, ProjectUploadForm, UserUpdateProfile, UserUpdate, ProjectUploadForm, RatingForm
import datetime as dt
from .models import Project, Profile, Rating
from .serializers import profileSerializer
from .permissions import IsAdminOrReadOnly

# Signup views here.
def signup(request):
    registered = False

    if request.method == "POST":
        registration_form = SignUpForm(data=request.POST)

        if registration_form.is_valid():
            # Grab user form and save to db
            registration_form.save()
            return redirect('/')
            # Grab password hash it then save to db
            user.set_password(user.password)
            user.save()

            registered = True

        else: 
            print(registration_form.errors)
    else:
        registration_form = SignUpForm()

    return render(request, 'user/registration.html', {'registration_form':registration_form}, {"registered":registered})

# Login

# Index views code
def index(request):
    new_project_form = ProjectUploadForm()
    project = Project.objects.all()
    rating_form = RatingForm()
    return render(request, 'index.html', {"project":project[::-1], "rating_form":rating_form})


# Profile views.
def profile(request):
    current_user = request.user
    new_project_form = ProjectUploadForm()
    return render(request, 'user/profile.html')

# Upload Project view here
def newproject(request):
    new_project_form = ProjectUploadForm()

    if request.method == "POST":
        new_project_form = ProjectUploadForm(request.POST,request.FILES)

        if new_project_form.is_valid():
            # Grab user form and save to db
            image = new_project_form.save(commit = False)
            image.user = request.user
            image.save()
            return redirect('/')
    else:
        new_project_form = ProjectUploadForm()
        # profile_form = UserProfileForm()

    return render(request, 'user/newproject.html', {"new_project_form":new_project_form})

# Update profile views here
def updateprofile(request):
  if request.method == 'POST':
    user_form = UserUpdateProfile(request.POST,instance=request.user)
    profile_form = UserUpdate(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('/profile')
  else:
    user_form = UserUpdateProfile(instance=request.user)
    profile_form = UserUpdate(instance=request.user.profile) 
  params = {
    'user_form':user_form,
    'profile_form':profile_form
  }
  return render(request,'user/updateprofile.html',params)

def uploadproject(request):
    new_project_form = ProjectUploadForm()

    if request.method == "POST":
        new_project_form = ProjectUploadForm(request.POST,request.FILES)

        if new_project_form.is_valid():
            # Grab user form and save to db
            project = new_project_form.save(commit = False)
            project.user = request.user
            project.save()
            return redirect('/')
    else:
        new_project_form = ProjectUploadForm()
        # profile_form = UserProfileForm()

    return render(request, 'instagram/image_form.html', {"new_project_form":new_project_form}, )


