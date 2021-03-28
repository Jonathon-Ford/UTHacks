from django.contrib import admin
 
 
from .models import Articles, ArticlesRating

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
 
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(ArticlesRating)
