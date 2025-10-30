from django.db import models

# Modèles à venir pour les entrepreneurs

class Entrepreneur(models.Model):
    nom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=150)
    secteur = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.entreprise})"
