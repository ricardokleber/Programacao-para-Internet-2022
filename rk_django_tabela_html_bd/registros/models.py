from django.db import models

class Registro(models.Model):
  nome = models.CharField(max_length=30)
  telefone = models.IntegerField()

  def __str__(self):
    return self.nome
