from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize 
from django.views import View
from datetime import datetime
from strava.models.perfil import Pefil

from django.shortcuts import render

def index(request):
    return render(request, "base.html", {"message": "bem-vindo"})


def primeira_view(request):
    mensagem = "Boa noite DEV I"

    return HttpResponse(mensagem, status=200)


class PrimeiraView(View):
    
    @staticmethod
    def get (request):
        mensagem = request.META['REMOTE_ADDR']
        return HttpResponse(mensagem, status=200)
    

class SaudacaoView(View):

    @staticmethod
    def get(request): 
        agora = datetime.now()
        mensagem = 'Boa noite'

        if 12 > agora.hour > 6:
            mensagem = 'Bom dia'
    
        elif 0 < agora.hour <= 6:
         mensagem = 'Boa madrugada'

    
        html = f'<html><body><h1>{mensagem.capitalize()} visitante!'\
            f'<br />{agora.strftime('%d/%m/%Y - %H:%M')} </h1></body></html>'
    
        return HttpResponse(html)


def saudacao(request):
    agora = datetime.now()
    mensagem = 'Boa noite'

    if 12 > agora.hour > 6:
        mensagem = 'Bom dia'
    
    elif 0 < agora.hour <= 6:
        mensagem = 'Boa madrugada'

    
    html = f'<html><body><h1>{mensagem.capitalize()} visitante!'\
            f'<br />{agora.strftime('%d/%m/%Y - %H:%M')} </h1></body></html>'
    
    return HttpResponse(html)


def nome(request, name):
    exemplo = Pefil.objects.find_by_nome(name)
    return HttpResponse(exemplo[0], status=200)


class NomeView(View):
    
    @staticmethod
    def get(request, name):
        exemplo = Pefil.objects.find_by_nome(name)
        return HttpResponse(exemplo[0], status=200)