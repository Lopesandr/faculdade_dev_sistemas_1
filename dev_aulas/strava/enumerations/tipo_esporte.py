from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEsporte(models.TextChoices):
    # django banco front
    RUN = "Corrida", _("Corrida")
    TRAIL_RUN = "Corrida de trilhas", _("Corrida de trilhas")
    WAL = "Caminhada", _("Caminhada")
    HIT = "Treino de alta intesidade", _("Treino de intesidade")
    STRENGTH = "Treino de força", _("Treino de força")
    CARDIO = "Treino Aerópico", _("Treino Aerópico")
    SWIMMING = "Natação", _("Natação")