from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, blank=False, default='Post Title')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        pass

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_comments')

    content = models.TextField(verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment:{self.content:20} by {self.author.username} under {self.post.title}"
    
    def get_absolute_url(self):
        pass

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} liked by {self.user.username}"
    
    