# Generated by Django 4.1.7 on 2023-03-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regiones', '0002_paises_sigla_pais_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='codigo_departamento',
            field=models.CharField(max_length=20, verbose_name='Codigo del Departamento'),
        ),
    ]
