from rest_framework import serializers
from workout.models.treinoModel import Treino
from workout.serializers.exercicioSerializer import ExercicioSerializer


class TreinoSerializer(serializers.ModelSerializer):
    exercicios = ExercicioSerializer(many=True, required=False)

    class Meta:
        model = Treino
        fields = ['id', 'usuario', 'nome', 'descricao', 'exercicios', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'criado_em', 'atualizado_em']

    def create(self, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        treino = Treino.objects.create(**validated_data)

        # passa o treino no contexto para o ExercicioSerializer
        for ex_data in exercicios_data:
            serializer = ExercicioSerializer(data=ex_data, context={'treino': treino})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return treino
