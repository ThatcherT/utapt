from django.db import models
from django.contrib.auth.models import User
import os
from django.conf.global_settings import MEDIA_ROOT
# Create your models here.
class RoommateProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField(max_length=500)
    WORKOUT = (
        ('Y', 'Yes, I workout.'),
        ('N', "No, I don't workout"),
        ('O', "Occasionally, I workout.")
    )
    workout = models.CharField(max_length=1, choices = WORKOUT)
    SCHOOL = (
        ('E', 'Cockrell School of Engineering'),
        ('L', 'School of Liberal Arts'),
        ('M', 'Mccombs School of Business'),
        ('N', 'School of Natural Sciences'),
        ('S', 'School of Social Work'),
    )
    school = models.CharField(max_length=1, choices = SCHOOL)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField( max_length=1, choices = GENDER)
    def __str__(self):
        return self.name


