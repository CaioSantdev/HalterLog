from rest_framework import serializers
from workout.models.exercicioModel import Exercicio
from workout.serializers.serieSerializer import SerieSerializer


class ExercicioSerializer(serializers.ModelSerializer):
    series = SerieSerializer(many=True, required=False)

    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'grupo_muscular', 'series']
        read_only_fields = ['id']

    def create(self, validated_data):
        series_data = validated_data.pop('series', [])
        treino = self.context.get('treino')  # Treino vem do TreinoSerializer
        if not treino:
            raise serializers.ValidationError({"treino": ["Treino context not provided."]})
        
        # cria o exercício já vinculado ao treino
        exercicio = Exercicio.objects.create(treino=treino, **validated_data)
        
        # cria as séries vinculadas ao exercício
        for serie_data in series_data:
            exercicio.series.create(**serie_data)

        return exercicio
