from django.conf import settings
from django.db import models
 
 
class Articles(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)

    Rating = models.FloatField()
    Review = models.TextField(default=' ')
    ratedate = models.DateTimeField()
    rated = models.BooleanField(default=False)
 