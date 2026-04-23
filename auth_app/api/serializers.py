from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from profile_app.models import UserProfile
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=UserProfile.TypeChoices.choices)
    class Meta:
        model = User
        fields = ['id','username','email','password','repeated_password','type']

    def validate(self, data):
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already  exist")
        return value
    def create(self, validated_data):
        user_type = validated_data.pop('type') 
        validated_data.pop('repeated_password')
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            UserProfile.objects.create(user=user, type=user_type)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get("request"), 
                username=username, 
                password=password
            )
            if not user:
                raise serializers.ValidationError("Login data don't match", code="authorization")
        else:
            raise serializers.ValidationError("You need to add email and password", code="authorization")
        
        attrs["user"] = user
        return attrs