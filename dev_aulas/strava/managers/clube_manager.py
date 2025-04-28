from django.db import models

class ClubeManager(models.Manager):
    def por_pais(self, pais):
        return self.filter(pais__iexact=pais)

    def por_website(self, url):
        return self.filter(url__iexact=url)

    def por_esporte(self, esporte):
        return self.filter(esporte__iexact=esporte)
