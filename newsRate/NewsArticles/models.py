from django.conf import settings
from django.db import models
 

class Articles(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title 


class ArticlesRating(models.Model):
    ratedDate = models.DateTimeField()
    ReviewTitle = models.CharField(max_length=100)
    ArticlesTitle = models.ForeignKey(Articles, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(default='Write you review here')
    ratedDate = models.DateTimeField()
    
    def __str__(self):
        return self.ReviewTitle

