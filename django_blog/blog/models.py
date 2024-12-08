from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model() #using the get_user_model method for decoupling

# Create your models here.

#* Models to be used in the blog web app
class Post(models.Model):
    """
    This is a model representing a database table that houses all our blog post articles.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        """"String Representation of a Post Object. Returns the title of the post"""
        return self.title
    

    class Meta:
        ordering = ['title']




from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    """This is an optional Extension of the User Model"""

    bio = models.TextField(help_text='Tell us about yourself', null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return f"{self.user.username}"
    
    def get_absolute_url(self):
        """"""
        return reverse('profile-manager', kwargs={'pk':self.user.pk})