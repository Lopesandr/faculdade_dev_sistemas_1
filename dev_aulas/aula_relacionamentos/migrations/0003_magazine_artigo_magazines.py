# Generated by Django 5.0 on 2025-04-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_relacionamentos', '0002_reporter_artigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='magazines',
            field=models.ManyToManyField(to='aula_relacionamentos.magazine'),
        ),
    ]
