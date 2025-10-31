from rest_framework import serializers
from workout.models.serieExecutadaModel import SerieExecutada

class SerieExecutadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieExecutada
        fields = ['id', 'sessao', 'exercicio', 'numero', 'repeticoes', 'peso', 'observacao', 'data_execucao']
        read_only_fields = ['id', 'data_execucao']
