from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def search_view(request, *args, **kwargs):
    return render(request, "search.html", {})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'