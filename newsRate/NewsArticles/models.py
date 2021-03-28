from django.conf import settings
from django.db import models
 
 
class Articles(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Rating = models.FloatField()
    Review = models.TextField(default=' ')
    RatedDate = models.DateTimeField()
 
