from rest_framework import serializers
from offers_app.models import Offer, OfferDetail
from django.contrib.auth import get_user_model

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username']

class OfferDetailSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        coerce_to_string=False
    )
    class Meta:
        model = OfferDetail
        fields = ['id','title','revisions','delivery_time_in_days','price','features','offer_type']

class OfferDetailLinkSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = OfferDetail
        fields = ['id', 'url']

    def get_url(self, obj):
        return f"/offerdetails/{obj.id}/"

class OfferSerializer(serializers.ModelSerializer):

    details = OfferDetailSerializer(many=True)
    class Meta:
        model = Offer
        fields = ['id','title','image','description','details']

    def validate_details(self, value):
        if len(value) !=3:
            raise serializers.ValidationError("Ein Offer muss genau 3 Details enthalten!")
        return value
    
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        user = self.context['request'].user
        offer = Offer.objects.create(user=user, **validated_data)
        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)
            
        return offer
    
class OfferListSerializer(serializers.ModelSerializer):
    details = OfferDetailLinkSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_details = UserDetailsSerializer(source='user', read_only=True)

    min_price = serializers.SerializerMethodField()
    min_delivery_time = serializers.SerializerMethodField()

    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    class Meta:
        model = Offer
        fields = ['id','user','title','image','description','created_at','updated_at','details','min_price','min_delivery_time','user_details']

    def get_min_price(self, obj):
        prices = [detail.price for detail in obj.details.all()]
        return min(prices) if prices else 0 

    def get_min_delivery_time(self,obj):
        times = [detail.delivery_time_in_days for detail in obj.details.all()]
        return min(times) if times else 0