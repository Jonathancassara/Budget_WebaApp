# frontend/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from datetime import datetime

def index(request):
    return render(request, 'frontend/index.html')

def gestion(request):
    return render(request, 'frontend/gestion.html')

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

def modifier_transaction(request, transaction_id):
    """
    Vue pour modifier une transaction existante.
    """
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        transaction.nom = request.POST.get('nom')
        transaction.commentaire = request.POST.get('commentaire', '')
        transaction.date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
        transaction.montant = float(request.POST.get('montant'))
        transaction.devise = request.POST.get('devise')
        transaction.solde = request.POST.get('solde')
        transaction.recurrente = request.POST.get('recurrente') == 'on'

        # Enregistrer les modifications
        transaction.save()
        return redirect('transactions_list')  # Rediriger vers la liste des transactions

    return render(request, 'frontend/modifier_transaction.html', {'transaction': transaction})

def compte(request):
    """
    Vue pour afficher le solde du compte et le solde à venir.
    """
    # Transactions passées (date <= aujourd'hui)
    transactions_passees = Transaction.objects.filter(date__lte=date.today())
    solde_actuel = sum(
        transaction.montant if transaction.solde == 'CREDIT' else -transaction.montant
        for transaction in transactions_passees
    )

    # Transactions futures (date > aujourd'hui)
    transactions_futures = Transaction.objects.filter(date__gt=date.today())
    solde_futur = sum(
        transaction.montant if transaction.solde == 'CREDIT' else -transaction.montant
        for transaction in transactions_futures
    )

    solde_a_venir = solde_actuel + solde_futur

    return render(request, 'frontend/compte.html', {
        'solde_actuel': solde_actuel,
        'solde_a_venir': solde_a_venir,
        'transactions_futures': transactions_futures,
    })