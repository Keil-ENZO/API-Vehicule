from django.db import models

# Create your models here.
from django.db import models

class Concession(models.Model):
    nom = models.CharField(max_length=255)
    numero_siret = models.CharField(max_length=14, blank=True, null=True)
    code_postal = models.CharField(max_length=5)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    marque = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    chevaux = models.IntegerField()
    immatriculation = models.CharField(max_length=10, unique=True)
    date_mise_en_service = models.DateField()
    concession = models.ForeignKey(Concession, related_name="vehicules", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"