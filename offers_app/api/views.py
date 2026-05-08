from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OfferSerializer, OfferDetailSerializer
from offers_app.models import Offer, OfferDetail
from .permissions import IsBusinessUserOrReadOnly

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = [IsAuthenticated, IsBusinessUserOrReadOnly]
    serializer_class  = OfferSerializer

class OfferDetailView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OfferDetailSerializer
    lookup_field = 'pk' 
