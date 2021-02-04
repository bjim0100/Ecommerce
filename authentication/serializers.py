from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from authentication.models import ProfileModel, UserList


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, validators=[validate_password], required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

        # def validate(self, attrs):
        #     if User.objects.filter(email=attrs['email']).exists():
        #         raise serializers.ValidationError({'email', 'Email is already in use'})
        #     return super().validate(attrs)

        # def create(self, validated_data):
        #     return User.objects.create_user(validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    User = serializers.StringRelatedField(read_only=True,many=True)

    class Meta:
        model = ProfileModel
        fields = [
            'profile_pic',
            'name',
            'location',
            'phone_number',
            'gender',
            'user'
        ]


class UserlistSerializer(serializers.ModelSerializer):

    class Meta:
        Model = User
        fields = ['username',
                  'email'
                  ]