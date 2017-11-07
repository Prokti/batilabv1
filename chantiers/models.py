from django.db import models
from profil.models import Profil
from django.contrib.auth.models import User
import os, random

# Create your models here.

def renommage(Fichier, nom):
    aleatoire = random.random()
    nom_fichier = os.path.splitext(nom)[0]    
    return "{}--{}--{}".format(Fichier.chantier.name, nom_fichier, aleatoire)



class Chantier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def mesMessages(self):
        return self.message_set.all()

    def mesFichiers(self):
        return self.fichier_set.all()
    


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Marche(models.Model):

    name = models.CharField(max_length=100)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marche_doc = models.FileField(upload_to='')
    devis_doc = models.FileField(upload_to='') 


class Message(models.Model):
    contenu = models.TextField(verbose_name="Message")
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    #users = models.ManyToManyField(User)

    def __str__(self):
        return self.contenu

class Fichier(models.Model):
    name = models.CharField(max_length=100)
    fichier_path = models.FileField(upload_to=renommage)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class CalculeMaison(models.Model):
    name = models.CharField(max_length=100)
    longueur_ext = models.FloatField()
    largueur_ext = models.FloatField()
    
    
    def __str__(self):
        return self.name

    def cal_surface_plancher(self):
        total = self.longueur_ext * self.largueur_ext
        return str(total)
     





