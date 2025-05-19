from django.urls import path
import strava.views as views 
from strava.views import * 
app_name = 'strava'

urlpatterns = [ 
    path('teste', views.primeira_view, name="primeira_view"),
    path('classe_teste', PrimeiraView.as_view(), name="primeira_classe_view"),
    path('html', views.saudacao, name='saudacao'),
    path('classe_saudacao', SaudacaoView.as_view(), name="classe_saudacao_view"),
    path('funcao/<str:name>', views.nome, name="nome"),
    path('classe_nome/<str:name>', NomeView.as_view(), name="classe_nome"),

]