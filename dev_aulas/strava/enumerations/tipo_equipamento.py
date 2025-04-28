from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEquipamento(models.TextChoices):

    SNEAKER = "Tenis", _("Tenis")
    BIKE  = "Bicicleta", _("Bicicleta")
    SMART_DEVICE = "Dispositivo inteligente", _("Dispositivo inteligente")