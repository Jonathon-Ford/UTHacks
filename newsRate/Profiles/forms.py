from django import forms
from .models import Profiles
from django.contrib.auth.forms import UserCreationForm


class ProfilesEditForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = [
            'name',
            'qualification'
        ]


class ProfilesForm(UserCreationForm):
    class Meta:
        model = Profiles
        fields = ['email', 'password1', 'password2', 'name', 'qualification']
