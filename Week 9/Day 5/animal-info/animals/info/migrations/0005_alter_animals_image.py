# Generated by Django 4.0 on 2021-12-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_animals_image_animals_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='image',
            field=models.ImageField(null=True, upload_to='photo_animals/'),
        ),
    ]
