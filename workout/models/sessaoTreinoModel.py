from django.db import models
from django.conf import settings
from .treinoModel import Treino

class SessaoTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='sessoes')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessoes_treino')
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Sessao - {self.usuario.username} ({self.treino.nome}) {self.data_inicio.date()}"