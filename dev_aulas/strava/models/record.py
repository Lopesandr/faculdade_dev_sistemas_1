from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models 
from strava.enumerations.tipo_esporte import TipoEsporte
from strava.enumerations.tipo_marca import TipoMarca
import datetime


class Record(BaseModel):

    nome = models.CharField(
        max_length=20, null=False, blank=False,
        validators = [MinLengthValidator(2)],
        help_text = "Nome do record, ente 2 e 20 caracteres",
        verbose_name = "Nome Record",
    )

    tipo_marca = models.CharField(
        max_length = 30,
        choices = TipoMarca,
        default = TipoMarca.m100,
        help_text = "A marca em distância atingida.",
        verbose_name = "Tipo da marca",
    )

    tipo_esporte = models.CharField(
        max_length = 30,
        choices = TipoEsporte,
        default = TipoEsporte.RUN,
        help_text = "Tipo de esporte realizado",
        verbose_name = "Tipo de esporte",
    ) 

    ritmo = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        help_text = "Ritmo realizado",
        verbose_name = "Ritmo"

    )
    durqcao = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        help_text = "Duracaçao do record",
        verbose_name = "Duração"

    )

    
