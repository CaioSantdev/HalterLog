from rest_framework import viewsets, permissions
from accounts.models.userModel import User
from accounts.serializers.userSerializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]