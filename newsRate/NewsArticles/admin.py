admin
from django.contrib import admin
 
 
from .models import ArticleRating, Article
 
admin.site.register(ArticleRating)
admin.site.register(Article)
