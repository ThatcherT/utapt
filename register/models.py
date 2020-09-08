from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from west.models import Apartment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.TextField(max_length=100, blank=True) #make choice later
    smoke = models.CharField(max_length=3, blank=True)
    aboutme = models.TextField(max_length=500, blank=True)
    favorites = models.ManyToManyField(Apartment)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()