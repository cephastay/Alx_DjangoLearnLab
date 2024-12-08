from django.db import models

from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

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

    tags = TaggableManager(to='Tag', related_name='post_tag_set')

    def __str__(self):
        """"String Representation of a Post Object. Returns the title of the post"""
        return self.title

    def get_absolute_url(self):
        """"""
        return reverse('post-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['title']

class Comment(models.Model):
    """Model of Comments"""
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE,related_name='post_comments')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=True, auto_now_add=True)

    def __str__(self):
        return f"{self.content} by {self.author.username} under {self.post.title}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.post.pk})
    
class Tag(models.Model):

    name = models.CharField(unique=True, max_length=50)
    posts = models.ManyToManyField(Post, related_name='post_tags')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-tag', kwargs={'tag_name':self.name})


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