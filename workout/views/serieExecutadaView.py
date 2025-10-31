from rest_framework import viewsets, permissions
from workout.models.serieExecutadaModel import SerieExecutada
from workout.serializers.serieExecutadaSerializer import SerieExecutadaSerializer

class SerieExecutadaViewSet(viewsets.ModelViewSet):
    queryset = SerieExecutada.objects.all()
    serializer_class = SerieExecutadaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SerieExecutada.objects.filter(sessao__usuario=self.request.user)
