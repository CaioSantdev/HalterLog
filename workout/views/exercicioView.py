from rest_framework import viewsets, permissions
from workout.models.exercicioModel import Exercicio
from workout.serializers.exercicioSerializer import ExercicioSerializer

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [permissions.AllowAny]

