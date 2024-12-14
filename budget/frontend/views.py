# frontend/views.py
from django.shortcuts import render, redirect
from .models import Transaction
from datetime import datetime

def index(request):
    return render(request, 'frontend/index.html')

def gestion(request):
    return render(request, 'frontend/gestion.html')



def transactions_list(request):
    transactions = Transaction.objects.all().order_by('-date')  # Dernières transactions d'abord
    return render(request, 'frontend/transactions_list.html', {'transactions': transactions})


def ajouter_transaction(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        commentaire = request.POST.get('commentaire', '')
        date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
        montant = float(request.POST.get('montant'))
        devise = request.POST.get('devise')
        solde = request.POST.get('solde')
        recurrente = request.POST.get('recurrente') == 'on'

        # Créer la transaction
        Transaction.objects.create(
            nom=nom,
            commentaire=commentaire,
            date=date,
            montant=montant,
            devise=devise,
            solde=solde,
            recurrente=recurrente,
        )
        return redirect('transactions_list')  # Redirection vers la liste des transactions

    return render(request, 'frontend/ajouter_transaction.html')

