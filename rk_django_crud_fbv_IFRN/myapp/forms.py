from django import forms
from django.db.models.base import Model
from django.forms import fields
from myapp.models import Registros

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        # fields = ['nome', 'email', 'telefone']
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
        }