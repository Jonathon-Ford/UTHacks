from django.urls import path
from .views import article_list
 
 
urlpatterns = [
    path('Articles', article_list, name='articles'),
]
