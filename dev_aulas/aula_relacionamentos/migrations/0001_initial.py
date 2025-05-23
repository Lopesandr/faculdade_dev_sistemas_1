# Generated by Django 5.0 on 2025-04-07 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('number', models.CharField(max_length=100, verbose_name='Numero de passaporte')),
                ('data_emissao', models.DateField(verbose_name='Data de emissão')),
                ('data_expiracao', models.DateField(verbose_name='Data de expiração')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aula_relacionamentos.person')),
            ],
        ),
    ]
