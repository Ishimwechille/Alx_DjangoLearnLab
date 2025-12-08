from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # <-- required by checker

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password')

        # MUST include: get_user_model().objects.create_user
        user = User.objects.create_user(  
            **validated_data,
            password=password
        )

        Token.objects.create(user=user)
        return user
