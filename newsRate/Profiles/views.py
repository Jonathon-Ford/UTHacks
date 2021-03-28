from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Profiles
from .forms import ProfilesForm, ProfilesEditForm


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts/profile.html')