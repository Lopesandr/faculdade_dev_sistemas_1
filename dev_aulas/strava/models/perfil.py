from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models 
from strava.enumerations.genero import Genero
from strava.validators.funcoes import validar_idade_minima
from django.utils.timezone import now
from .clube import Clube
import datetime


class Pefil(BaseModel):

    email = models.EmailField(
        max_length=100,
        validators = [MinLengthValidator(10)],
        verbose_name="Emal",
        help_text= "Informe um e-mail válido, minimo 10 caracters e maximo 100"
    )

    nome = models.CharField(
            max_length=100, blank=False, null=False
            ,validators = [MinLengthValidator(10)]    
            ,verbose_name="Nome"
            ,help_text="Inserir nome completo do usuário"
    )

    cpf = models.CharField(
        max_length=11,
        validators= [MinLengthValidator(11)],
        verbose_name="CPF",
        help_text="Insira um cpf contendo 11 caracters"
    )

    senha = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(5)],
        verbose_name="Senha",
        help_text="Insira uma senha, minimo 5 caracters e maximo 10 caracters."

    )

    data_nasc = models.DateField(   
        validators=[validar_idade_minima],
        verbose_name="Data de nascimento",
        help_text="Digite a data de nascimento"
    )

    local = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        verbose_name="Local",
        help_text="Insira o local onde mora, minimo 3 caracters e maximo 100"

    )

    pais = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        verbose_name="Pais",
        help_text="Insira o pais onde mora, minimo 3 caracters e maximo 100"
    )

    genero =  models.CharField(
        max_length=50,
        choices=Genero,
        default=Genero.WOMAN,
        verbose_name="Genero",
        help_text="Insira o seu genero"

    )


    peso = models.FloatField(
        verbose_name="Insira o peso",
        help_text="Insira o seu peso"
    )


    pagina_pessoal = models.URLField(
        max_length=150, 
        blank=True,
        null=False,
        verbose_name="Pagina pessoa",
        help_text="Informe o link da sua página pessoal"
    )

    biografia = models.CharField(
        max_length=1000,
        blank=True,
        null= True,
        verbose_name="Biografia",
        help_text="Insira sua biografia",

    )

    premimun = models.BooleanField(
        verbose_name="Premium",
        default=True
    )

    membro_desde = models.DateField(
        verbose_name="Membro desde", 
        help_text="Data em que se tornou membro",
        default=now
    )

    clube = models.ForeignKey(
        Clube,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="Clube"
    )

    def __str__(self):
        return self.nome
    
    def find_by_nome(self, nome):
        pass