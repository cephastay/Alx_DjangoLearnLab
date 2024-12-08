from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileManagementView.as_view(), name='profile-manager'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('home/', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='posts')
]