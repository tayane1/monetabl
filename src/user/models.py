from django.db import models

# Create your models here.

class User(models.Model):
    pseudo = models.CharField(max_length=50, unique=True)  # Champ pour le pseudo
    password = models.CharField(max_length=100)  # Champ pour le mot de passe
    dateCreation = models.DateTimeField(auto_now_add=True)  # Date de création automatiquement ajoutée
    
    def __str__(self):
        return self.pseudo  # Retourne le pseudo de l'utilisateur en stringr
    
    
    
    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'  # Pluralisation du nom de la classe en français
