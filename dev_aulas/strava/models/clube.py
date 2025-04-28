from django.core.validators import MinLengthValidator
from strava.enumerations.tipo_esporte import TipoEsporte
from strava.managers.clube_manager import ClubeManager
from .base_model import BaseModel
from django.db import models 


class Clube(BaseModel): 

    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)], 
        verbose_name="Nome",
        help_text="Informe o nome do Clube, minimo 3 caracters, maximo 100"
    )

    
    local = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        verbose_name="Local",
        help_text="Insira o local onde mora, minimo 3 caracters e maximo 100"

    )

    pais = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        verbose_name="Pais",
        help_text="Insira o pais onde mora, minimo 3 caracters e maximo 100"
    )

    tipo_esporte = models.CharField(
        max_length = 30,
        choices = TipoEsporte,
        default = TipoEsporte.RUN,
        help_text = "Tipo de esporte realizado",
        verbose_name = "Tipo de esporte",
    ) 

    biografia = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Biografia",
        help_text="Informe o a biografia do clube"
    )

    objects = ClubeManager()

    def __str__(self): 
        return self.nome   