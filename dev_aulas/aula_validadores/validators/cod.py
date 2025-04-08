from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _ 
from django.utils.deconstruct import deconstructible

@deconstructible
class CodValidator:

    def __init__(self, cod=0000000000):
        self.cod = cod
    
    def __call__(self, valor):
        if valor == self.cod:
            raise ValidationError(_("Valor inválidp"),
                                  params={"valor": valor},
                                  code = 'invalid')
        

    
    def __eq__(self, other):
        return(
                isinstance(other, CodValidator)
                and self.cod == other.cod
        )
        