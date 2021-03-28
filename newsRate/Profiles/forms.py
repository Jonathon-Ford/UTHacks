from django import forms
from .models import Profiles


class ProfilesEditForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = {
            'name',
            'qualification',
        }


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = {'name', 'qualification'}
