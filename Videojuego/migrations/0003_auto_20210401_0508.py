# Generated by Django 3.1.7 on 2021-04-01 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Videojuego', '0002_auto_20210401_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edades',
            old_name='nombre',
            new_name='nombre2',
        ),
    ]
