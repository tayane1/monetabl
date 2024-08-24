from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    pseudo = models.CharField(max_length=50, unique=True)  # Champ pour le pseudo
    password = models.CharField(max_length=100)  # Champ pour le mot de passe
    dateCreation = models.DateTimeField(auto_now_add=True)  # Date de création automatiquement ajoutée
