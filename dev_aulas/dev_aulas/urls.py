"""
URL configuration for dev_aulas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from dev_aulas.views.estatica import index
from dev_aulas.views.contact import ConcactView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('strava/', include('strava.urls')),
    # Aula 26/05 
    path('classe/contato/', ConcactView.as_view(), name="class_contact")
]
