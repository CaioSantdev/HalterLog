from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from accounts.serializers.authSerializer import RegisterSerializer, MeSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model

class RegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user":MeSerializer(user).data,
            "acess": str(refresh.access_token),
            "refresh": str(refresh),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    

class MeView(RetrieveUpdateAPIView):
    serializer_class = MeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user