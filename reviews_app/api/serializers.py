from rest_framework import serializers
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", read_only=True)
    class Meta:
        model = Review
        fields = ['id','business_user','reviewer','rating','description','created_at','updated_at']
        read_only_fields = ['reviewer']

    def validate(self, data):
        reviewer = self.context['request'].user
        business_user = data.get('business_user')
        if business_user:
            if not hasattr(business_user, 'profile') or business_user.profile.type != 'business':
                raise serializers.ValidationError(
                    {"business_user": "You can write only for business Profile users"}
                )
            if reviewer == business_user:
                raise serializers.ValidationError(
                    "You can not write own review"
                )
            if Review.objects.filter(reviewer=reviewer, business_user=business_user).exists():
                raise serializers.ValidationError(
                    "You have allready one review "
                )
        return data
    
class UpdateReviewSerializer(ReviewSerializer):
    class Meta(ReviewSerializer.Meta):
        read_only_fields = ['id','business_user','reviewer','created_at','updated_at']

