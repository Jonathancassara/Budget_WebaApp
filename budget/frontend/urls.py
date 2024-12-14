# frontend/urls.py
from django.urls import path
from .views import index,gestion

urlpatterns = [
    path('', index, name='index'),
    path('gestion/', gestion, name='gestion'),
]