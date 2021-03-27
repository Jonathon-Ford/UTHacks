from django.db import models

# Create your models here.


class Profiles(models.Model):
    name = models.TextField()
    areaOfExpertise = models.TextField(default='none')
    level = models.IntegerField()