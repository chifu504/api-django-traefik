from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    # Asegurándonos de que la contraseña tenga al menos 8 caracteres y no más de 128, y que no pueda ser leída
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        # Lista de todos los campos que se pueden incluir en una solicitud o respuesta
        fields = ['id', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Utilizando el método `create_user` que escribimos anteriormente en UserManager para crear un nuevo usuario.
        return User.objects.create_user(**validated_data)
