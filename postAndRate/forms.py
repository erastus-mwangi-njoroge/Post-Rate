from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Rating, Profile

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profilePicture']

class ProjectUploadForm(forms.ModelForm):
 
    class Meta:
        model = Project
        fields = ["title","description","link","image"]

class RatingUploadForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ["design","usability","content"]