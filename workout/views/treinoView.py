from rest_framework import viewsets, permissions
from workout.models.treinoModel import Treino
from workout.serializers.treinoSerializer import TreinoSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer
    permission_classes = [permissions.AllowAny]
