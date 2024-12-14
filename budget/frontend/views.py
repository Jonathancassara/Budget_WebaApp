# frontend/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from datetime import datetime

def index(request):
    return render(request, 'frontend/index.html')

def transactions_list(request):
    """
    Vue pour afficher la liste des transactions.
    """
    transactions = Transaction.objects.all().order_by('-date')  # Trier par date décroissante
    return render(request, 'frontend/transactions_list.html', {'transactions': transactions})


def ajouter_transaction(request):
    """
    Vue pour ajouter une nouvelle transaction.
    """
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        commentaire = request.POST.get('commentaire', '')
        date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
        montant = float(request.POST.get('montant'))
        devise = request.POST.get('devise')
        solde = request.POST.get('solde')
        recurrente = request.POST.get('recurrente') == 'on'

        # Créer une nouvelle transaction
        Transaction.objects.create(
            nom=nom,
            commentaire=commentaire,
            date=date,
            montant=montant,
            devise=devise,
            solde=solde,
            recurrente=recurrente,
        )
        return redirect('transactions_list')  # Rediriger vers la liste des transactions

    return render(request, 'frontend/ajouter_transaction.html')


def supprimer_transaction(request, transaction_id):
    """
    Vue pour supprimer une transaction.
    """
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions_list')

    return render(request, 'frontend/supprimer_transaction.html', {'transaction': transaction})
