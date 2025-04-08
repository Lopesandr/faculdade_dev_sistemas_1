from django.contrib import admin
from aula_relacionamentos.models import Person, Passport, Reporter, Artigo, Magazine
# Register your models here.

classes = (Person, Passport, Artigo, Reporter, Magazine)
admin.site.register(classes)