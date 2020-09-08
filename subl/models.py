from django.db import models
from django.contrib.auth.models import User
import os
from django.conf.global_settings import MEDIA_ROOT
# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Sublease(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    aptname = models.TextField()
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=30)
    price = models.IntegerField()
    rooms = models.IntegerField()
    sqft = models.IntegerField()
    contact = models.CharField(max_length=100)
    # images = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    dateposted = models.DateField()
    GENDER = (
                 ('M', 'Males'),
                 ('F', 'Females'),
                 ('E', 'Any')
    )
    opento = models.CharField( max_length=1, choices = GENDER)

    NEG = (
        ('Y', 'Negotiable'),
        ('N', 'Non-Negotiable')
    )
    negotiable = models.CharField(max_length=1, choices=NEG)

    AREAS = (
        ('W', 'West Campus'),
        ('N', 'North Campus'),
        ('R', 'Riverside'),
        ('O', 'Other')
    )
    area = models.CharField(max_length=1, choices=AREAS)
    def __str__(self):
        return self.name
