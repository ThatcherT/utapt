from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    price = models.IntegerField()

    AREAS = (
        ('W', 'West Campus'),
        ('N', 'North Campus'),
        ('R', 'Riverside')
    )
    area = models.CharField(max_length=1, choices=AREAS)

    def __str__(self):
        return self.name
class Review(models.Model):
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    review = models.TextField()

    def __str__(self):
        return self.name