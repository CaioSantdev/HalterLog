from rest_framework import serializers
from workout.models.exercicioModel import Exercicio
from workout.serializers.seriaSerializer import SerieSerializer

class ExercicioSerializer(serializers.ModelSerializer):

    series = SerieSerializer(many=True,read_only=False,required=False)

    class Meta:
        model = Exercicio
        fields = ['id', 'treino', 'nome', 'grupo_muscular', 'series']

    def create(self,validated_data):
        series_data = validated_data.pop('series',[])
        exercicio = Exercicio.objects.create(**validated_data)
        for serie_data in series_data:
            exercicio.series.create(**serie_data)

        return exercicio
    
    def update(self, instance, validated_data):
        series_data = validated_data.pop("series",[])
        instance.nome = validated_data.get('nome',instance.nome)
        instance.grupo_muscular= validated_data.get('grupo_muscular',instance.grupo_muscular)
        instance.save()

        if series_data:
            instance.series.all().delete()
            for serie_data in series_data:
                instance.series.create(**serie_data)
            return instance