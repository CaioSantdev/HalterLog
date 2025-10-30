from rest_framework import serializers
from accounts.models.userModel import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'dataNascimento',
            'peso',
            'altura'
        ]
        read_only_fields = ['id']
        