from rest_framework import serializers
from offers_app.models import Offer, OfferDetail


class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        fields = ['title','revisions','delivery_time_in_days','price','features','offer_type']

class OfferSerializer(serializers.ModelSerializer):

    details = OfferDetailSerializer(many=True)

    class Meta:
        model = Offer
        fields = ['title','image','description','details']

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
    
