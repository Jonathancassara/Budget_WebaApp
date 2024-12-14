# frontend/admin.py
from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'montant', 'devise', 'date', 'solde')
    list_filter = ('devise', 'solde', 'date')
    search_fields = ('nom', 'commentaire')
