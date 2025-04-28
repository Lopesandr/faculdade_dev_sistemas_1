from django.core.validators import MinLengthValidator
from strava.enumerations.tipo_esporte import TipoEsporte
from .atividade import Atividade
from .base_model import BaseModel
from django.db import models

class Desafio(BaseModel):

    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        verbose_name="Nome",
        help_text="Nome do desafio, minimo 5 caracters, maximo 50"
    )

    desafio_ini = models.DateField(
        verbose_name="Data inicial",
        help_text="Data inicio"
    )

    desafio_fim = models.DateField(
        verbose_name="Data fim",
        help_text="Data fim"
    )

    tipo_esporte = models.CharField(
        max_length=100,
        choices=TipoEsporte,
        default=TipoEsporte.CARDIO,
        verbose_name="Tipo esporte",
        help_text="Tipo esporte"
    )

    visao_geral = models.TextField(
        verbose_name="Visão geral",
        help_text="Visão geral",
        blank=True,
        null=True
    )

    selo = models.CharField(
        max_length=5,
        verbose_name="Selo",
        help_text="Selo"
    )

    atividade = models.ManyToManyField(
        Atividade,
        verbose_name="Atividade",
        help_text="Atividade",
        related_name="atividade"
    )


    def __str__(self):
        return self.nome