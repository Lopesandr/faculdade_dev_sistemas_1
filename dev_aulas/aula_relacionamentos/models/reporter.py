from django.db import models

class Reporter(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nome}, {self.email}"