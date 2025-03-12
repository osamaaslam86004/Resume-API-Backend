from rest_framework import serializers
from api_auth.authentication import CustomUser
from django.contrib.auth.password_validation import validate_password
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


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class LogoutResponseSerializer(serializers.Serializer):
    status = serializers.CharField(
        help_text='Status message, e.g., "Successful Logout"'
    )


class InvalidTokenResponseSerializer(serializers.Serializer):
    status = serializers.CharField(help_text="token not valid because user is inactive")
    code = serializers.CharField(help_text="Token Invalid")


class TokenErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(help_text="Token already blacklisted")
    code = serializers.CharField(help_text="Token Error")


class InternalServerErrorSerializer(serializers.Serializer):
    status = serializers.CharField(help_text="failed to update user profile")
    code = serializers.CharField(help_text="Server Error")
