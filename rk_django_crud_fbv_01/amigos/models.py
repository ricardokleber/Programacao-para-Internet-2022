from django.db import models

class amigos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.IntegerField()
    class Meta:
        verbose_name_plural = "Amigos"
    def __str__(self):
        return self.nome