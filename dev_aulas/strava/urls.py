from django.urls import path
import strava.views.exemplo  as views_
import strava.views.estatica as views 

from strava.views import * 
app_name = 'strava'

urlpatterns = [ 
    path('teste', views.primeira_view, name="primeira_view"),
    path('classe_teste', PrimeiraView.as_view(), name="primeira_classe_view"),
    path('html', views.saudacao, name='saudacao'),
    path('classe_saudacao', SaudacaoView.as_view(), name="classe_saudacao_view"),
    path('funcao/<str:name>', views.nome, name="nome"),
    path('classe_nome/<str:name>', NomeView.as_view(), name="classe_nome"),
    path('exemplo/fuction',views_.exemplo_list , name="exemplo_fuction_list"),
    path('exemplo/fuction/read/<int:pk>', views_.exemplo_detail, name='exemplo_fuction_read'),
    path('exemplo/classe/read/<int:pk>', views_.ExemploDetailView.as_view(), name='exemplo_classe_read'),
    path('exemplo/fuction/delete/<int:exemplo_id>', views_.delete, name='exemplo_fuction_delete'),
    path('exemplo/class/delete/<int:exemplo_id>', views_.ExemoloDeleteView.as_view(), name='exemplo_class_delete'),



    # path('exemplo/classe', ExemploList.as_view(), name="exemplo_classe_list")

]