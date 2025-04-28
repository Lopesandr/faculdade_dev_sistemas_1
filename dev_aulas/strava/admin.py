from django.contrib import admin
from strava.models import Record, Pefil, Clube, LinkSociaisClube, Equipamento, Atividade, Desafio, DesafioAtividade, DesafioTempo, DesafioAtividadeTempo
# Register your models here.

classes = (Record, Pefil, Clube, LinkSociaisClube, Equipamento, Atividade, Desafio, DesafioAtividade, DesafioTempo, DesafioAtividadeTempo)
admin.site.register(classes)