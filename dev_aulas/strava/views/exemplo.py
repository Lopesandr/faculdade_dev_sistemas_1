from strava.models.perfil import Pefil
from django.shortcuts import render, redirect
from django.core.serializers import serialize 
from strava.models.perfil import Pefil


def exemplo_list(request):
    exemplos = Pefil.objects.all()
    context = {'exemplos': exemplos,}
    return render(request,  'exemplo/list.html', context)