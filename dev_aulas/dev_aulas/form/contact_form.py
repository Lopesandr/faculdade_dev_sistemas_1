from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# Aula 26/05 

class ContactForm(forms.Form):
    subject = forms.CharField(label='Assunto',
                              max_length=100,
                              validators=[MinLengthValidator(3)],
                              help_text="Digite o assunto da mensagem"
                            )      
    sender = forms.EmailField(label="E-mail",
                              help_text="Digite seu endereço de e-mail principal")

    message = forms.CharField(label="Mensagem",
                              help_text="Digite sua mensagem",
                              widget=forms.Textarea)

    cc_myself = forms.BooleanField(required=False,
                                   label="Deseja receber uma cópia?") 