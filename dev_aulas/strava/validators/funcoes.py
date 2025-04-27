from django.core.exceptions import ValidationError
from django.utils import timezone



def validar_idade_minima(valor): 
    hoje = timezone.now().date()
    idade = hoje.year - valor.year - ((hoje.month, hoje.day) < (valor.month, valor.day))

    if idade < 18:
        raise ValidationError('O usuário deve ter pelo menos 18 anos de idade.')
    
def validar_inicial_url_website(url: str):
    
    if  url.startswith('www.'): 
        pass
    else:
        raise ValidationError('A url deve inicar com www.')
    
def validar_inicial_url_instagram(url: str):
    
    if  url.startswith('www.instagram.com'): 
        pass
    else:
        raise ValidationError('A url deve inicar com www.instagram.com')
    

def validar_inicial_url_facebook(url: str):
    
    if  url.startswith('www.facebook.com'): 
        pass
    else:
        raise ValidationError('A url deve inicar com www.facebook.com')
    
