from django.shortcuts import render, redirect
from .form import amigoForm
from .models import amigos

def lista_amigos(request):
    amigo = amigos.objects.all()
    todos = {'amigo':amigo}
    return render(request, 'lista_amigos.html', todos)

def criar_amigo(request):
    form = amigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_amigos")
    todos = {'form_amigo': form}
    return render(request, 'criar_amigo.html', todos)

def atualizar_amigo(request, id_amigo):
    todos = {}
    amigo = amigos.objects.get(pk = id_amigo)
    form = amigoForm(request.POST or None, instance=amigo)
    if form.is_valid():
        form.save()
        return redirect("lista_amigos")
    todos['form_amigo'] = form
    todos['amigo'] = amigo
    return render(request, 'criar_amigo.html', todos)

def deletar_amigo(request, id_amigo):
    amigo = amigos.objects.get(pk = id_amigo)
    amigo.delete()
    return redirect('lista_amigos')