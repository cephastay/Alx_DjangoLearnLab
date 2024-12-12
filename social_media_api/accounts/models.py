from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    """
    This model extends the Abstract user in django to customize some additional fields
    """
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='media/', default='default.png')
    followers = models.ManyToManyField('CustomUser', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass
