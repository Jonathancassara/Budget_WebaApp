# frontend/urls.py
from django.urls import path
from .views import (
    index,
    gestion,
    transactions_list,
    ajouter_transaction,
    supprimer_transaction,
    modifier_transaction,
    compte
    )


urlpatterns = [
    path('', index, name='index'),
    path('gestion/', gestion, name='gestion'),
    path('transactions/', transactions_list, name='transactions_list'),
    path('transactions/ajouter/', ajouter_transaction, name='ajouter_transaction'),
    path('transactions/supprimer/<int:transaction_id>/', supprimer_transaction, name='supprimer_transaction'),  # Supprimer une transaction
    path('transactions/modifier/<int:transaction_id>/', modifier_transaction, name='modifier_transaction'),
    path('compte/', compte, name='compte'),  # Page du compte
]