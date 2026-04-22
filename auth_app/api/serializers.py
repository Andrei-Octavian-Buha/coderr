from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from profile_app.models import UserProfile
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    repeated_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','password','reoeated_password']

    def create(self, validated_data):

        user_type = validated_data.pop('type') 

        with transaction.atomic():
            user = User.objects.create(**validated_data)
            UserProfile.objects.create(user=user, type=user_type)
        return user