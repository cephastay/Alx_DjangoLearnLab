from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from blog.forms import RegisterForm, ProfileManagementForm
from blog.models import Post, UserProfile

class RegisterView(CreateView):
    """Ä view to create new user instances"""

    template_name = 'register.html'
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileManagementView(LoginRequiredMixin, UpdateView):
    """A view to manage user profiles requires users to LogIn"""
    template_name = 'profile_management.html'
    model = User
    form_class = ProfileManagementForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileManagementForm(instance=user)
        context['user'] = self.request.user
        return context
    
    def get_success_url(self) -> str:
        return reverse ('profile')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        user_bio = form.cleaned_data.get('bio')
        user_photo = form.cleaned_data.get('profile_picture')
        user = self.request.user
        
        profile = user.profile  
        profile.bio = user_bio
        profile.profile_picture = user_photo
        profile.save()

        user.save()
        
        return super().form_valid(form)

class HomeView(TemplateView):
    template_name ='home.html'

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post

