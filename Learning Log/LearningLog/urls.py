""" Define the URL patterns for learning logs """
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path(r'^$', views.index, name='index'),
]