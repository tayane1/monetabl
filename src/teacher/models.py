from django.db import models

# Create your models here.


class Teacher(models.Model):
    lastName = models.CharField(max_length=50)  # Champ pour le nom
    firstName = models.CharField(max_length=50)  # Champ pour le prénom
    birthDay = models.DateField()  # Champ pour la date de naissance
    city = models.CharField(max_length=100)  # Champ pour la ville
    telephon = models.CharField(max_length=15)  # Champ pour le téléphone
    vacant = models.BooleanField(default=True)
    subjectSign = models.CharField(max_length=100)
    nextCours = models.CharField(max_length=200)
    topicNextMeeting = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.lastName # Retourne le nom et prénom du enseignant en string

class Meta:
    verbose_name = 'Professeur'
    verbose_name_plural = 'Professeurs'  # Pluralisation du nom de la classe en français
