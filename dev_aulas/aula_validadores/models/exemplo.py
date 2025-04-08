import random
import string
from aula_validadores.validators.funcoes import validate_par
from aula_validadores.validators.cod import CodValidator
from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError 
from django.utils.translation import gettext as _


class Exemplo(BaseModel):
    cod = models.CharField(max_length=20, 
                           validators=[MinLengthValidator(10), validate_par,  CodValidator("4444444444")])
    
    nome = models.CharField(max_length=15, validators=[MinLengthValidator(3)])

    def save(self, *args, **kwargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kwargs)

    def clean(self):
        if self.cod == '1111111111' and self.nome == 'IFRS Restinga':
            raise ValidationError({"nome": "Combinação de nome e codigo errada",
                                  "cod": "Combinação de nome e código e errado"},
                                  code="error01")
