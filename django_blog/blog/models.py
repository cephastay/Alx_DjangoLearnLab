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