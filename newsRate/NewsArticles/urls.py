from django.urls import path

from . import admin
from .views import article_list
from ..Pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_list, name='article-list'),
    path('home/', home_view, name='home'),
]
