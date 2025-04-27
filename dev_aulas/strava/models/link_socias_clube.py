from django.core.validators import MinLengthValidator
from strava.validators.funcoes import validar_inicial_url_website, validar_inicial_url_instagram, validar_inicial_url_facebook
from .clube import Clube
from .base_model import BaseModel
from django.db import models 

class LinkSociaisClube(BaseModel):

    website = models.URLField(
        max_length=100,
        validators=[MinLengthValidator(4),validar_inicial_url_website],
        verbose_name="Url do website", 
        help_text="Digite uma url com minimo de 4 caracters e no maximo 100 caracters"
        
    )

    instagram = models.URLField(
        max_length=100,
        validators=[MinLengthValidator(4),validar_inicial_url_instagram],
        verbose_name="Url do instagram", 
        help_text="Digite uma url do instagram com minimo de 4 caracters e no maximo 100 caracters"
        
    )

    facebook = models.URLField(
        max_length=100,
        validators=[MinLengthValidator(4),validar_inicial_url_facebook],
        verbose_name="Url do facebook", 
        help_text="Digite uma url do facebook com minimo de 4 caracters e no maximo 100 caracters"
        
    )

    other = models.URLField(
        max_length=100,
        blank= True,
        null=True,
        validators=[MinLengthValidator(4)],
        verbose_name="Outra url", 
        help_text="Digite uma url com minimo de 4 caracters e no maximo 100 caracters"
        
    )

    clube = models.OneToOneField(
        Clube, 
        on_delete=models.CASCADE,
        related_name="links_sociais"
    )


    def __str__(self):
        return f"Website: {self.website}\nInstagram: {self.instagram}"