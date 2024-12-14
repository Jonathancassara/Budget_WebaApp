# frontend/urls.py
from django.urls import path
from .views import transactions_list, ajouter_transaction, supprimer_transaction

urlpatterns = [
    path('', transactions_list, name='transactions_list'),  # Page d'accueil
    path('transactions/', transactions_list, name='transactions_list'),
    path('transactions/ajouter/', ajouter_transaction, name='ajouter_transaction'),
    path('transactions/supprimer/<int:transaction_id>/', supprimer_transaction, name='supprimer_transaction'),
]
