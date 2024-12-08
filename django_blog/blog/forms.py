from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    """"A form that extends the User Creation Form to include Email during registration"""

    email = forms.EmailField(help_text='Please valid emails only', required=True)

    class Meta:
        model = User
        fields = ['username', ]

class ProfileManagementForm(UserChangeForm):
    """A custom form that allows users to edit their profile details"""
    bio = forms.CharField(max_length=500, help_text='Enter your bio here...', required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = ['password']

from blog.models import Post, Comment

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']