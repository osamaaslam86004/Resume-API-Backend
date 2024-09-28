from rest_framework import serializers
from custom_simplejwt.serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "password", "is_staff", "is_active"]

    def create(self, validated_data):

        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            is_active=validated_data.get("is_active", None),
            is_staff=validated_data.get("is_staff", None),
        )

        return user


class TokenClaimObtainPairSerializer(CustomTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["user"] = user.username

        return token
