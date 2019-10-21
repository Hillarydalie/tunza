from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Project, Profile

# This is the registration form for awwwards
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Email Required!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectUploadForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_image','project_name','project_caption', 'project_url']

class UserUpdateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic','bio']

class UserUpdate(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class ProjectUpload(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['project_name','project_caption', 'project_image', 'project_url']