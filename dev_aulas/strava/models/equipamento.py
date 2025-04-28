from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from strava.enumerations.tipo_equipamento import TipoEquipamento
from strava.enumerations.tipo_esporte import TipoEsporte
from django.db import models

class Equipamento(BaseModel):
    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        verbose_name="Nome",
        help_text="Nome do equipamento, minimo 5 caracters, maximo 50"
    )

    marca = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        verbose_name="Marca",
        help_text="Marca do equipamento, minimo 5 caracters, maximo 50"
    )

    modelo = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        verbose_name="Modelo",
        help_text="Modelo do equipamento, minimo 5 caracters, maximo 50"
    )

    apelido = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        verbose_name="Apelido",
        help_text="Apelido do equipamento, minimo 5 caracters, maximo 50"
    )

    tipo_equipamento = models.CharField(
        max_length= 100,
        verbose_name="Tipo equipamento",
        help_text="Tipo equipamento",
        choices=TipoEquipamento,
        default=TipoEquipamento.BIKE
    )

    tipo_esporte = models.CharField(
        max_length= 100,
        verbose_name="Tipo esporte",
        help_text="Tipo esporte",
        choices=TipoEsporte,
        default=TipoEsporte.CARDIO
    )

    distancia_total = models.FloatField(
        verbose_name="Distancia total",
        help_text="Distancia total",
        validators=[MinValueValidator(0)]
    )

    distancia_prevista = models.IntegerField(
        verbose_name="Distancia prevista",
        help_text="Distancia prevista",
        validators=[MinValueValidator(400)]
    )

    peso = models.FloatField(
        verbose_name= "Peso",
        help_text="Peso",
        validators=[MinValueValidator(0)]
    )

    notas = models.TextField(
        verbose_name="Notas",
        help_text="Notas",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome