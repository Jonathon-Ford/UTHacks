from django.urls import path
from .views import article_list

app_name = 'NewsArticles'
urlpatterns = [
    path('', article_list, name='article-list'),
]
