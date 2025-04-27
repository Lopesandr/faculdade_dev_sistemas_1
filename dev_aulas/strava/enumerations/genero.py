from django.utils.translation import gettext_lazy as _
from django.db import models

class Genero(models.TextChoices):
    # django banco front
    RUN = "Corrida", _("Corrida")
    MAN = "Homem", _("Homem")
    WOMAN = "Mulher", _("Mulher")
    NON_BINARY = "Não binário", _("Não binário")
    NOT_INFORMED = "Não informado", _("Não informado")

