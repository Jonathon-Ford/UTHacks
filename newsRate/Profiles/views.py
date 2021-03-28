from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfilesEditForm


def register_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form:': form}
    return render(request, 'accounts/register.html', context)


def edit_profile(request):
    form = ProfilesEditForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)