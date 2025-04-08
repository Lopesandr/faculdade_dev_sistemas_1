from django.db import models
from .person import Person

class Passport(models.Model):
    number = models.CharField(max_length=100, 
                              verbose_name="Numero de passaporte")
    
    data_emissao = models.DateField(verbose_name="Data de emissão")
    data_expiracao = models.DateField(verbose_name="Data de expiração")
    pessoa = models.OneToOneField(Person, on_delete=models.CASCADE,
                                  primary_key=True)