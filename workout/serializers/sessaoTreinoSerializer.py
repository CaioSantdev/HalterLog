from rest_framework import serializers
from workout.models.sessaoTreinoModel import SessaoTreino
from workout.serializers.serieExecutadaSerializer import SerieExecutadaSerializer

class SessaoTreinoSerializer(serializers.ModelSerializer):
    series_executadas = SerieExecutadaSerializer(many=True, read_only=True)


class SessaoTreinoSerializer(serializers.ModelSerializer):
    series_executadas = SerieExecutadaSerializer(many=True, required=False)

    class Meta:
        model = SessaoTreino
        fields = ['id', 'treino', 'usuario', 'data_inicio', 'data_fim', 'observacoes', 'series_executadas']
        read_only_fields = ['id', 'data_inicio', 'data_fim']

    def create(self, validated_data):
        series_data = validated_data.pop('series_executadas', [])
        sessao = SessaoTreino.objects.create(**validated_data)
        for serie_data in series_data:
            sessao.series_executadas.create(**serie_data)
        return sessao
