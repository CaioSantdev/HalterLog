from rest_framework import serializers
from workout.models.serieModel import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = [
            'id', 'numero', 'tipo', 'repeticoes',
            'peso', 'descanso', 'observacao',
            'criado_em', 'atualizado_em'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']
