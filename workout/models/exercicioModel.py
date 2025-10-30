from django.db import models
from .treinoModel import Treino

class Exercicio(models.Model):


    GRUPOS_MUSCULARES = [
        ('PEITO', 'Peito'),
        ('COSTAS', 'Costas'),
        ('OMBROS', 'Ombros'),
        ('BICEPS', 'Bíceps'),
        ('TRICEPS', 'Tríceps'),
        ('QUADRICEPS', 'Quadriceps'),
        ('POSTERIOR', 'Posterior'),
        ('PANTURRILHAS', 'Panturrilhas'),
        ('ABD', 'Abdômen'),
        ('ANT. BRAÇOS', 'Ant Braços'),
        ('GLUTEOS', 'Gluetos'),
    ]

    treino = models.ForeignKey(Treino,on_delete=models.CASCADE,related_name='exercicios')
    name = models.CharField(max_length=256)
    grupo_muscular = models.CharField(
        max_length=20,
        choices=GRUPOS_MUSCULARES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nome} ({self.get_grupo_muscular_display() or 'Sem grupo'})"