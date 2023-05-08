from django.contrib import admin
from django.urls import path

from amigos.views import atualizar_amigo, criar_amigo, deletar_amigo, lista_amigos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", lista_amigos, name="lista_amigos"),
    path("lista_amigos/", lista_amigos, name="lista_amigos"),
    path("criar_amigo/", criar_amigo, name="criar_amigo"),
    path("atualizar_amigo/<int:id_amigo>", atualizar_amigo, name="atualizar_amigo"),
    path("deletar_amigo/<int:id_amigo>", deletar_amigo, name="deletar_amigo"),
]
