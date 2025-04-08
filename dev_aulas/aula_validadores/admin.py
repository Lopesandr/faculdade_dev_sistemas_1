from django.contrib import admin
from aula_validadores.models import Exemplo
# Register your models here.

classes = (Exemplo)
admin.site.register(classes)