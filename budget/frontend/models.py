# frontend/models.py
from django.db import models

class Transaction(models.Model):
    DEVISE_CHOICES = [
        ('EURO', 'Euro'),
        ('PLN', 'Polish Zloty'),
        ('USD', 'US Dollar'),
    ]

    SOLDE_CHOICES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]

    id = models.AutoField(primary_key=True)  # ID automatique
    nom = models.CharField(max_length=255, verbose_name="Nom")  # Nom de la transaction
    commentaire = models.TextField(blank=True, verbose_name="Commentaire")  # Description ou notes
    date = models.DateField(verbose_name="Date")  # Date de la transaction
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")  # Montant
    devise = models.CharField(max_length=4, choices=DEVISE_CHOICES, verbose_name="Devise")  # Devise utilisée
    solde = models.CharField(max_length=6, choices=SOLDE_CHOICES, verbose_name="Solde")  # Type de solde (Crédit/Débit)
    recurrente = models.BooleanField(default=False, verbose_name="Transaction récurrente")  # Si la transaction est récurrente

    def __str__(self):
        return f"{self.nom} - {self.montant} {self.devise} ({self.solde})"
