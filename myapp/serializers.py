from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from myapp.models import User, Ad
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'is_landlord', 'is_renter', 'password','re_password']
        extra_kwargs = {'password': {'write_only': True}}
        ordering = ['email']

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

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        ordering = ['email']

class UserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['id', 'name', 'email', 'date_joined', 'last_login', 'groups', 'user_permissions']
        ordering = ['email']


class AdSerializer(serializers.ModelSerializer):
    owner = StringRelatedField(read_only=True)
    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        ordering = ['-id']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long')
        if len(value) > 100:
            raise serializers.ValidationError('Title must be less than 100 characters long')
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Description must be less than 500 characters long')
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be a positive number')
        return value

    def validate_rooms(self, value):
        if value < 1:
            raise serializers.ValidationError('Number of rooms must be at least 1')
        return value

    def validate_type(self, value):
        if value not in [choice[0] for choice in Ad.TYPE_CHOICES]:
            raise serializers.ValidationError('Invalid type')
        return value

    def validate_state(self, value):
        if not re.match(r'^([a-zA-Z ]{2,50})$', value):
            raise serializers.ValidationError( "The state must be represented by alphabetic characters")
        return value

    def validate_city(self, value):
        if not re.match(r'^([a-zA-Z ]{2,50})$', value):
            raise serializers.ValidationError("The city must be represented by alphabetic characters")
        return value

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


