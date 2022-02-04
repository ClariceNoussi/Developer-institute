from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=100)
    photo = models.ImageField(upload_to='photo/%y/%m/%d/')
    price = models.IntegerField()
    description = models.TextField(blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    owner = models.ManyToManyField(User, related_name='owner_in_product')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('products')





#class Panier(models.Model):



#class Command(models.Model):
 #   products = models.ManyToManyField(Products, null=True)
  #  users = models.ManyToManyField(Users, null=True)


