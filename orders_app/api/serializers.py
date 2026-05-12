from rest_framework import serializers
from offers_app.models import OfferDetail
from orders_app.models import Order

class OrderSerializer(serializers.ModelSerializer):
    offer_detail = serializers.PrimaryKeyRelatedField(
        queryset=OfferDetail.objects.all(), 
        write_only=True
    )
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ",read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ",read_only=True)
    class Meta:
        model = Order
        fields = ['id','offer_detail','customer_user','business_user','title','revisions','delivery_time_in_days','price','features','offer_type','status','created_at','updated_at']
        read_only_fields = ['id','customer_user','business_user','title','revisions','delivery_time_in_days','price','features','offer_type','status']

    def create(self, validated_data):
        offer_detail = validated_data.pop('offer_detail')

        validated_data['customer_user'] = self.context['request'].user
        validated_data['business_user'] = offer_detail.offer.user
        validated_data['title'] = offer_detail.offer.title
        validated_data['revisions'] = offer_detail.revisions
        validated_data['delivery_time_in_days'] = offer_detail.delivery_time_in_days
        validated_data['price'] = offer_detail.price
        validated_data['features'] = offer_detail.features

        return Order.objects.create(offer_detail=offer_detail,**validated_data)

class OrderUpdateSerializer(OrderSerializer):
    class Meta(OrderSerializer.Meta):
        read_only_fields = ['id','customer_user','business_user','title','revisions','delivery_time_in_days','price','features','offer_type']

        