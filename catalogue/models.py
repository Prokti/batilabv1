from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

import sys
import os

# Create your models here.


class Groupe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=100)
    price_ht = models.FloatField()
    code = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.name

    def total(self):
        q1 = self.houseitem_set.all()

        # print(q1)
        # print('-----------------------')
        dict1 = {}

        for x in q1:
            r1 = q1.get(id=x.id)
            r2 = r1.houseattributeprice_set.all()
            # print(r1)
            for y in r2:
                dict1[y.house_attribute_value.name] = y.price_ht

        # print(dict1)
        return dict1

    def groupe(self):
        g = self.houseitem_set.all()

        resultat = {}

        for x in g:
            # print(x.groupe_id)
            g3 = g.filter(groupe_id=x.groupe_id)

            for y in g3:

                y1 = (y.houseattributeprice_set.all())

                for y2 in y1:

                    r1 = y2.house_item.groupe.name

                    if r1 in resultat:
                        resultat[r1].append(
                            {y2.house_attribute_value.name: y2.price_ht})

                    else:
                        resultat[r1] = [
                            {y2.house_attribute_value.name: y2.price_ht}]
                    
                    
        print(resultat)
        return resultat

    def prix_ttc(self):
        return self.price_ht * 1.20


class HouseAttribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HouseAttributeValue(models.Model):
    name = models.CharField(max_length=100)
    house_attribute = models.ForeignKey(
        HouseAttribute, on_delete=models.CASCADE)

    def __str__(self):
        return "{}  [{}]".format(self.name, self.house_attribute)


class HouseItem(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    variantes = models.ManyToManyField(
        HouseAttributeValue, through='HouseAttributePrice')

    def __str__(self):
        return "{} - {}".format(self.house, self.groupe)

   # class Meta:
    #    verbose_name = "Déclinaison Maison"


class HouseAttributePrice(models.Model):
    house_item = models.ForeignKey(HouseItem, on_delete=models.CASCADE)
    house_attribute_value = models.ForeignKey(
        HouseAttributeValue, on_delete=models.CASCADE)
    price_ht = models.FloatField()
    
    #content_object = GenericForeignKey("house_item", "price_ht")

    def calcule_ttc(self):
        self.price_ht * 1.20

    def __float__(self):
        return self.price_ht

    def __str__(self):
        return "{} - {}".format(self.house_item, self.house_attribute_value)


'''

class HouseVariante(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)    
    variante = models.ForeignKey(Variante, on_delete=models.CASCADE)
    price_ht = models.FloatField()
    

    def __str__(self):
        return self.house.name

    def mes_groupes(self):
        q1 = self.house.groupes.all()
        
        for e in q1:
            print(e.name)
            

    def calcule1(self):
        q1 = self.housevariante_set.values()
        print (q1)
        
        total_price_groupe = 0
        dict_groupe1 = {}
        dict_groupe2 = {}
        total_liste = []

        for x in q1:
            print(x)
            #return (cle)
            print (x.get("price_ht"))

            if x.get('groupe_id') == 1:
                
                y = x.get('variante_id')
                t = x.get('price_ht')
                dict_groupe1[y] = t

            else:
                y = x.get('variante_id')
                t = x.get('price_ht')
                dict_groupe2[y] = t


        print(dict_groupe1)
        print(dict_groupe2)

'''
'''


class PriceOption(models.Model):    
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    price_ht = models.FloatField()

    def __str__(self):
        return self.option.name

    def variante(self):
        q1 = self.house.price_ht
        q2 = self.price_ht
        return q1 + q2

    def variante2():
        q1 = Option.objects.filter(pk=1)
        return q1

'''


'''

class HouseVariantePrice(models.Model):
    house_variante = models.ForeignKey(HouseVariante, on_delete=models.CASCADE)
    variante = models.ForeignKey(Variante, on_delete=models.CASCADE)
    price_ht = models.FloatField()

    def __str__(self):
        return self.house_variante.groupe.name
'''
