from django_filters import rest_framework as filters
from offers_app.models import Offer

class OfferFilter(filters.FilterSet):
    """
    Custom filter set for the Offer model.
    
    Allows users to filter results by the creator's ID, a minimum price 
    threshold, and a maximum delivery time limit. These filters utilize 
    related fields from the OfferDetail model.
    """
    creator_id = filters.NumberFilter(field_name='user_id')
    min_price =	filters.NumberFilter(field_name='details__price',lookup_expr='gte')
    max_delivery_time = filters.NumberFilter(field_name='details__delivery_time_in_days',lookup_expr='lte')
    
    class Meta:
        model = Offer
        fields = ['creator_id','min_price','max_delivery_time']