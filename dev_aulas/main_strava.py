import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_aulas.settings')
django.setup()
from strava.models.clube import Clube

print(Clube._meta.get_field('tipo_esporte').choices)

c1 = Clube(
    nome="Clube de bike",
    local="Porto Alegre",
    pais="Brasil",
    tipo_esporte="Corrida",  # <- Aqui precisa ser um valor VÁLIDO do choices!
    biografia="TETS"  # <- Aqui também
)
c1.full_clean()
c1.save()
print(Clube._meta.get_field('tipo_esporte').choices)
print(Clube.objects.por_pais("Brasil"))