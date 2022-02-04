# Generated by Django 4.0.1 on 2022-01-28 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produits', '0006_products_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='owner',
            field=models.ManyToManyField(related_name='owner_in_product', to=settings.AUTH_USER_MODEL),
        ),
    ]