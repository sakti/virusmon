from django.shortcuts import render


def index(request):
    """home page"""
    return render(request, 'base.html')
