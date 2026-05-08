from rest_framework import serializers
from offers_app.models import Offer, OfferDetail


class OfferDetailSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        coerce_to_string=False
    )
    class Meta:
        model = OfferDetail
        fields = ['id','title','revisions','delivery_time_in_days','price','features','offer_type']

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
        offer = Offer.objects.create(**validated_data)
        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)
            
        return offer
    
