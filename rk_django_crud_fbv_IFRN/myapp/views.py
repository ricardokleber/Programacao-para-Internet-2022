from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import RegistrosForm
from myapp.models import Registros
from django.contrib import messages

def home(request):
    data = Registros.objects.all()

    if request.method == 'POST':
        form = RegistrosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inclusão Realizada !')
            form = RegistrosForm()
    else:
        form = RegistrosForm()
    return render(request, 'myapp/home.html', {'form':form, 'data':data})

def delete(request, id):
    registro_a_apagar = Registros.objects.get(pk=id)
    registro_a_apagar.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
        registro_a_atualizar = Registros.objects.get(pk=id)
        editando = RegistrosForm(request.POST, instance=registro_a_atualizar)
        if editando.is_valid():
            editando.save()
    else:
        registro_a_atualizar = Registros.objects.get(pk=id)
        editando = RegistrosForm(instance=registro_a_atualizar)
    return render(request, 'myapp/update.html', {'form':editando})

