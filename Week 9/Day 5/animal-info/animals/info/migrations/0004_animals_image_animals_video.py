# Generated by Django 4.0 on 2021-12-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_animals_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='animals',
            name='image',
            field=models.ImageField(null=True, upload_to='photo_animals'),
        ),
        migrations.AddField(
            model_name='animals',
            name='video',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
