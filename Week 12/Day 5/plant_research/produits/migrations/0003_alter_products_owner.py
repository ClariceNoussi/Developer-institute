# Generated by Django 4.0.1 on 2022-01-24 03:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produits', '0002_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='owner',
            field=models.ManyToManyField(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
