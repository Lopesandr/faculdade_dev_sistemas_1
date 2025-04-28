from django.db import models

class PerfilManager(models.Manager):

    def por_pais(self, pais):
        return self.filter(pais=pais)
    
    def por_website(self, url):
        return self.filter(url=url)
    
    def por_esporte(self, esporte):
        return self.filter(esporte=esporte)