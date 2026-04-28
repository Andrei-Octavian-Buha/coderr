from rest_framework import serializers
from profile_app.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username', read_only=True)


    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'user', 'username', 'first_name', 'last_name', 
            'file', 'location', 'tel', 'description', 
            'working_hours', 'type', 'email', 'created_at'
        ]
        read_only_fields = ['type']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user
        if user_data:
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name',user.last_name)
            user.email = user_data.get('email', user.email)
            user.save()
        return super().update(instance, validated_data)
    
class BusinessListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = UserProfile
        fields = [
            'user', 'username', 'first_name', 'last_name', 
            'file', 'location', 'tel', 'description', 
            'working_hours', 'type'
        ]
        read_only_fields = ['type']

class CustomerListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    uploaded_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", source='created_at',read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = UserProfile
        fields = [
            'user', 'username', 'first_name', 'last_name', 
            'file', 'uploaded_at', 'type'
        ]
        read_only_fields = ['type']