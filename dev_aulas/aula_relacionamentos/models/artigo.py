from django.db import models
from .reporter import Reporter
from .magazine import Magazine

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    data_pub = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return self.titulo