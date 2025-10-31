from django.db import models
from .exercicioModel import Exercicio

class Serie(models.Model):
    ROTULOS_SERIE = [
    ('WS', 'Working Set'),
    ('DESC', 'Série de Descanso'),
    ('FAIL', 'Série até a Falha'),
    ('BO', 'Backoff Set'),
    ]

    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE,
        related_name='series'
    )

    numero = models.PositiveBigIntegerField(
        help_text='Número da série (1,2,3...)',
        default=3
    )
    repeticoes = models.PositiveIntegerField(
        help_text="Número de repetições planejadas", default=8
    )
    tipo = models.CharField(
        max_length=10,
        choices=ROTULOS_SERIE,
        blank=True,
        null=True,
        help_text="Tipo da série (opcional)"
    )

    peso = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Peso usado em kg"
    )
    descanso = models.PositiveIntegerField(
        default=60,
        help_text="tempo de descanso entre a serie"
    )

    observacao = models.TextField(
        blank=True,
        null=True,
        help_text="Notas adicionais sobre a série"
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        tipo = self.get_tipo_display() or "Sem rótulo"
        return f"Série {self.numero}: {self.repeticoes} reps, {self.peso or 0}kg ({tipo})"