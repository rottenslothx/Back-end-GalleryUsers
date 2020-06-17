from rest_framework import serializers
from .models import Users


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'gender']


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name')
