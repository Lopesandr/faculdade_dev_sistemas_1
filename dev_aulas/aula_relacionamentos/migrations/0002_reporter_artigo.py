# Generated by Django 5.0 on 2025-04-08 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_relacionamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data_pub', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula_relacionamentos.reporter')),
            ],
        ),
    ]
