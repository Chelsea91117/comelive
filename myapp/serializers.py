from rest_framework import serializers
from myapp.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re


class UserRegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 're_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        name = data.get('name')

        if not re.match('^.{0,20}$', name):
            raise serializers.ValidationError({"name": "Ensure this field has no more than 20 characters."})

        password = data.get("password")
        re_password = data.get("re_password")

        if password != re_password:
            raise serializers.ValidationError({"password": "Passwords don't match."})

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('re_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
