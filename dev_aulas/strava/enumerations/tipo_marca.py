from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoMarca(models.TextChoices):
    # django banco front
    m100 = "100M", _("100 metros")
    m400 = "200M", _("400 metros")
    km1 = "1KM", _("1 KM")
    km5 = "5KM", _("5 KM")
    km15 = "15KM", _("15 KM")
    km20 = "20KM", _("20 KM")
    meia = "Meia Maratona", _("Meia Maratona") 
    km30 = "30KM", _("30 KM")
    maratona = "Maratona", _("Maratona")
    longa_distancia = "Longa Distancia", _("Longa Distancia")
    longa_duracao = "Longa Duração", _("Longa Duração")