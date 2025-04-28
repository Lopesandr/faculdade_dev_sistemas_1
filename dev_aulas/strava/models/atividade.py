from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from strava.enumerations.tipo_esporte import TipoEsporte
from .equipamento import Equipamento
from django.db import models


class Atividade(BaseModel):

    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        verbose_name="Nome",
        help_text="Insira o nome da atividade, minimo 5 caracters, maximo 40"
    )

    observacao = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        validators=[MinLengthValidator(5)],
        verbose_name="Nome",
        help_text="Insira a observação da atividade, minimo 5 caracters, maximo 40"
    )

    data = models.DateField(
        verbose_name="Data",
        help_text="A data da atividade"
    )

    tipo_esporte = models.CharField(
        max_length= 100,
        choices=TipoEsporte,
        verbose_name="Tipo esporte",
        help_text="Tipo esporte",
        default=TipoEsporte.CARDIO
    )

    inicio = models.TimeField(
        verbose_name="Inicio da atividade",
        help_text="Inicio da atividade"
    )

    duracao = models.TimeField(
        verbose_name="Duração da atividade",
        help_text="Duração da atividade"
    )

    distancia = models.FloatField(
        verbose_name="Distancia",
        help_text="Distancia"
    )

    ritmo = models.TimeField(
        verbose_name="Ritmo",
        help_text="Ritmo"
    )

    calorias = models.IntegerField(
        verbose_name="Calorias",
        help_text="Calorias",
        validators=[MinValueValidator(0)],
        default=0
    )

    elevacao_total = models.IntegerField(
        verbose_name="Elevação total",
        help_text="Elevação total",
        default=0
    )

    equipamento = models.ManyToManyField(
        Equipamento, 
        related_name="equipamento"
    )

    def __str__(self):
        return self.nome