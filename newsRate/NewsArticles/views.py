from django.shortcuts import render
from .models import Articles
 
 
def article_list(request):
   context = {'Articles': Articles.Title.all()}
   return render(request, "article_list.html", context)
 