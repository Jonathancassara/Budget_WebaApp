# frontend/urls.py
from django.urls import path
from .views import index,gestion,ajouter_transaction, transactions_list

urlpatterns = [
    path('', index, name='index'),
    path('gestion/', gestion, name='gestion'),
    path('transactions/', transactions_list, name='transactions_list'),
    path('transactions/ajouter/', ajouter_transaction, name='ajouter_transaction'),
]

