from .base_model import BaseModel
from django.db import models 

class Person(BaseModel):
    nome = models.CharField(max_length=100, 
                            verbose_name = "Nome completo")
    
    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    