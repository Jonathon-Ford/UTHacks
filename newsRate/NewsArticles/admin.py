from django.contrib import admin

# Register your models here.
from .models import ArticleRating, Article

admin.site.register(ArticleRating)
admin.site.register(Article)
