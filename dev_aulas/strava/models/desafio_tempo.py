from django.core.validators import MinLengthValidator
from .desafio import Desafio
from django.db import models

class DesafioTempo(Desafio):

    meta_duracao = models.TimeField(
        verbose_name="Tempo da meta",
        help_text="Tempo da meta"
    )

    def __str__(self):
        return self.nome