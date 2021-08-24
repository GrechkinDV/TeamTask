from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    """ Account Serializer extends from default ModelSerializer """

    password = serializers.CharField(
        required=True,
        write_only=True,
        min_length=8,
        error_messages={
            "blank": "Введите пароль!",
            "min_length": "Пароль слишком короткий(меньше 8-ми символов)!"
        }
    )

    email = serializers.EmailField(
        required=True,
        write_only=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "name",
            "institution",
            "password",
            "date_joined",
            "last_login",
        ]         

        read_only_fields = ["id", "password", "date_joined", "last_login"]

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
