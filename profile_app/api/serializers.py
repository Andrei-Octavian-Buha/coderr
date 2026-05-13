from rest_framework import serializers
from profile_app.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Comprehensive serializer for detailed user profiles.
    
    Flattens data from both the Django User model (first name, last name, email) 
    and the UserProfile model. It handles complex nested updates to ensure 
    core user identity information is kept in sync with profile details.
    """
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
    """
    Optimized serializer for the business directory.
    
    Provides essential information for service providers, including 
    contact details, location, and operating hours for public display.
    """
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
    """
    Simplified serializer for customer listings.
    
    Focuses on basic identification and registration timestamps, 
    designed for administrative or community overview views.
    """
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