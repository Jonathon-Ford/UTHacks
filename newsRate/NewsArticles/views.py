from django.shortcuts import render
from .models import Article
 
 
def article_list(request):
   context = {'Article': Article.Title.all()}
   return render(request, "search.html", context)
 