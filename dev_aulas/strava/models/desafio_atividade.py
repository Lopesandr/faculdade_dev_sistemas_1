from django.core.validators import MinLengthValidator
from .desafio import Desafio
from django.db import models

class DesafioAtividade(Desafio):

    meta_duracao = models.IntegerField(
        verbose_name="Tempo de atividades",
        help_text="Tempo de atividades"
    )

    def __str__(self):
        return self.nome