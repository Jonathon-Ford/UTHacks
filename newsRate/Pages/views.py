from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def loggin_view(request, *args,**kwargs):
    return HttpResponse("<h1> Log in: </h1>")