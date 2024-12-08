from django.dispatch import receiver
from django.db.models.signals import post_save
from blog.models import UserProfile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """A signal for automatically creating user profiles when a user is registered"""
    if created:
        UserProfile.objects.create(user=instance)