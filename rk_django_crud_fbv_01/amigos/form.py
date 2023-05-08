from dataclasses import fields
from django.forms import ModelForm
from .models import amigos

class amigoForm(ModelForm):
    class Meta:
        model = amigos
        fields = ['nome', 'email', 'telefone']