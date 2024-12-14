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

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, verbose_name="Nom")
    commentaire = models.TextField(blank=True, verbose_name="Commentaire")
    date = models.DateField(verbose_name="Date")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")
    devise = models.CharField(max_length=4, choices=DEVISE_CHOICES, verbose_name="Devise")
    solde = models.CharField(max_length=6, choices=SOLDE_CHOICES, verbose_name="Solde")

    def __str__(self):
        return f"{self.nom} - {self.montant} {self.devise} ({self.solde})"
