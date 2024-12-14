# frontend/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def gestion(request):
    return render(request, 'frontend/gestion.html')