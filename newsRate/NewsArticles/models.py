from django.conf import settings
from django.db import models
 
 
class Articles(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.FloatField()
    review = models.TextField(default=' ')
    ratedDate = models.DateTimeField()
 
