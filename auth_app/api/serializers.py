from django.contrib.auth.models import User
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

    def create(self, validated_data):
        user_type = validated_data.pop('type') 
        validated_data.pop('repeated_password')
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            UserProfile.objects.create(user=user, type=user_type)
        return user