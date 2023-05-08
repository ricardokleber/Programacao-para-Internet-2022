from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Registro

def testando(request):
  todos = Registro.objects.all().order_by('nome')
  template = loader.get_template('template.html')
  context = {
    'listagem': todos,
  }
  return HttpResponse(template.render(context, request))
