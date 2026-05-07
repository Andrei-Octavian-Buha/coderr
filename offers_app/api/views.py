from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OfferSerializer
from offers_app.models import Offer

class GetOfferList(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = []
    serializer_class  = OfferSerializer
