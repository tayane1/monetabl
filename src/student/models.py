from django.db import models

# Create your models here.

class Student(models.Model):
    lastName = models.CharField(max_length=50)  # Champ pour le nom
    firstName = models.CharField(max_length=50)  # Champ pour le prénom
    gender = models.CharField(max_length=6 , default=None) #
    birthDay = models.DateField()  # Champ pour la date de naissance
    city = models.CharField(max_length=100)  # Champ pour la ville
    telephon = models.CharField(max_length=15)  # Champ pour le téléphone
    classRoom = models.CharField(max_length=50)
    matricule = models.CharField(max_length=20, unique=True)