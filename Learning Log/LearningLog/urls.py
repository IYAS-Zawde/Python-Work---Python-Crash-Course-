""" Define the URL patterns for learning logs """
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
]