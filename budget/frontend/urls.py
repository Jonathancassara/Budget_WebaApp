# frontend/urls.py
from django.urls import path
from .views import index,gestion,ajouter_transaction, transactions_list,supprimer_transaction

urlpatterns = [
    path('', index, name='index'),
    path('gestion/', gestion, name='gestion'),
    path('transactions/', transactions_list, name='transactions_list'),
    path('transactions/ajouter/', ajouter_transaction, name='ajouter_transaction'),
    path('transactions/supprimer/<int:transaction_id>/', supprimer_transaction, name='supprimer_transaction'),  # Supprimer une transaction
]

