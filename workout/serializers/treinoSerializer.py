from rest_framework import serializers
from workout.models.treinoModel import Treino
from workout.serializers.exercicioSerializer import ExercicioSerializer

class TreinoSerializer(serializers.ModelSerializer):
    exercicios = ExercicioSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Treino
        fields = ['id', 'usuario', 'nome', 'descricao', 'exercicios', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'criado_em', 'atualizado_em']

    def create(self, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        treino = Treino.objects.create(**validated_data)
        for ex_data in exercicios_data:
            series_data = ex_data.pop('series', [])
            exercicio = treino.exercicios.create(**ex_data)
            for serie_data in series_data:
                exercicio.series.create(**serie_data)
        return treino

    def update(self, instance, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.save()

        if exercicios_data:
            instance.exercicios.all().delete()
            for ex_data in exercicios_data:
                series_data = ex_data.pop('series', [])
                exercicio = instance.exercicios.create(**ex_data)
                for serie_data in series_data:
                    exercicio.series.create(**serie_data)
        return instance