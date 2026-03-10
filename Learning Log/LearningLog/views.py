from django.shortcuts import render


def index(request):
    """The Home page for Learning Log"""
    return render(request, 'index.html')