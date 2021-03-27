from django.conf import settings
from django.db import models


class ArticleRating(models.Model):
    star = models.FloatField()
    Rating = models.TextField(default=' ')
    ratedate = models.DateTimeField()
    ArticleRating = models.ForeignKey('self',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.Rating


class Article(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rates = models.ManyToManyField(ArticleRating)
    rated = models.BooleanField(default=False)

    def __str__(self):
        return self.Title




