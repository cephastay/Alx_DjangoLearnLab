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

from blog.models import Post, Comment, Tag
from taggit.forms import TagWidget
from django.forms import Textarea

class PostCreationForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=50,
        required=False,
        help_text='Add new tag',
        widget=TagWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            "content": Textarea(attrs={"cols": 80, "rows": 20}),
        }

    def save(self, commit = True):
        instance = super().save(commit)
        post_instance = instance.id
        tag = self.cleaned_data['tags']
        if tag:
            Tag.objects.create(name=tag, posts=post_instance)
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SearchForm(forms.Form):
    to_search = forms.CharField(
        max_length=150,
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Search...',

            }
        ))

    