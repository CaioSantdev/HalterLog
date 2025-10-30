from rest_framework import viewsets, permissions
from workout.models.serieModel import Serie
from workout.serializers.seriaSerializer import SerieSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = [permissions.AllowAny]