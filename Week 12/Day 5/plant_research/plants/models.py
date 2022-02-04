from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)

    def __repr__(self):
        return self.name


class Molecules(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, max_length=900)
    #structure_url = models.CharField(null=True, max_length=100)
    #description = models.TextField(blank=True)

    def __repr__(self):
        return self.name


class EconomicComments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)

    def __repr__(self):
        return self.name


class Plants(models.Model):
    id = models.AutoField(primary_key=True)
    scientificName = models.CharField(null=False, max_length=100)
    primaryCommonName = models.TextField(blank=True)
    generalDescription = models.TextField(blank=True)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, null=True)
    image_url = models.CharField(null=True, max_length=100)
    is_published = models.BooleanField(default=True)
    molecules = models.ManyToManyField(Molecules, related_name='molecules_in_plants')
    economicComments = models.ManyToManyField(EconomicComments, related_name='plants_in_diseases')

    def __repr__(self):
        return self.scientificName

    #def get_absolute_url(self):
     #   return reverse('plants')
