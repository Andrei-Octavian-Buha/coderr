from django_filters import rest_framework as filters
from reviews_app.models import Review

class ReviewFilter(filters.FilterSet):
    """
    Custom filter set for the Review model.
    
    Provides specialized filtering capabilities to retrieve reviews 
    based on the business user being reviewed or the specific reviewer 
    who authored the feedback.
    """
    business_user_id = filters.NumberFilter(field_name='business_user')
    reviewer_id = filters.NumberFilter(field_name='reviewer')

    class Meta:
        model = Review
        fields = ['business_user', 'reviewer_id']