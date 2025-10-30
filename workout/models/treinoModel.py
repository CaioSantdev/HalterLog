from django.db import models
from django.conf import settings

class Treino(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='treinos')
    nome = models.CharField(max_length=256)
    descricao = models.TextField(blank=True,null=True)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    def __str__(self):
        return f"Train-{self.nome} - {self.usuario.username}"