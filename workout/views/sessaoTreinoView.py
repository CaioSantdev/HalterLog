from rest_framework import viewsets, permissions
from workout.models.sessaoTreinoModel import SessaoTreino
from workout.serializers.sessaoTreinoSerializer import SessaoTreinoSerializer

class SessaoTreinoViewSet(viewsets.ModelViewSet):
    queryset = SessaoTreino.objects.all()
    serializer_class = SessaoTreinoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return SessaoTreino.objects.filter(usuario=self.request.user).order_by('-data_inicio')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)