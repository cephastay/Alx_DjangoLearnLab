from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from blog.forms import RegisterForm, ProfileManagementForm, PostCreationForm
from blog.models import Post, UserProfile

class RegisterView(CreateView):
    """Ä view to create new user instances"""

    template_name = 'register.html'
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileManagementView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        return self.request.user == self.get_object()

class HomeView(TemplateView):
    template_name ='home.html'


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostCreationForm

    def form_valid(self, form):
        post_author = self.request.user
        form.instance.author = post_author
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.has_perm('blog.add_post')
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'content']

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('posts')

    def is_owner(self):
        post = self.get_object()
        return self.request.user == post.author

    def test_func(self):
        return self.is_owner()
    

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_create_post'] = self.request.user.has_perm('blog.add_post')
        return context

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    
    


def dummy(request):
    if request.method == "POST":
        form = RegisterForm(instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(request, 'post_list.html', {'dummy':dummy})


