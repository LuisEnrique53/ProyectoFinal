# Generated by Django 3.1.7 on 2021-04-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videojuego', '0016_auto_20210422_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='ultimo_inicio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
