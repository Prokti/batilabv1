from django.db import models
from profil.models import Profil
from django.contrib.auth.models import User
import os
import random


def renommage(Fichier, nom):
    #date = Fichier.date()
    nom_fichier = os.path.splitext(nom)[0]
    return "{}/{}".format(Fichier.chantier.name, nom_fichier)


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


class CategorieFichier(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Message(models.Model):
    contenu = models.TextField(verbose_name="Message")
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    #users = models.ManyToManyField(User)

    def __str__(self):
        return self.contenu


class Fichier(models.Model):
    name_categorie = models.ForeignKey(CategorieFichier, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, auto_now=True)
    fichier_path = models.FileField(upload_to=renommage)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_categorie.name

