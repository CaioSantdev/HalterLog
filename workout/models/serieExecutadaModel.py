from django.db import models
from .sessaoTreinoModel import SessaoTreino
from .exercicioModel import Exercicio

class SerieExecutada(models.Model):
    sessao = models.ForeignKey(SessaoTreino, on_delete=models.CASCADE, related_name='series_executadas')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(default=1)
    repeticoes = models.PositiveIntegerField(default=8)
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    data_execucao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)
    
    def __str__(self): 
        return f"{self.exercicio.nome} - {self.peso}kg x {self.repeticoes} reps"