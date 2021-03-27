from django.db import models

# Create your models here.


class Profiles(models.Model):
    name = models.CharField(max_length=50)
    areaOfExpertise = models.TextField(default='none')
    level = models.IntegerField()