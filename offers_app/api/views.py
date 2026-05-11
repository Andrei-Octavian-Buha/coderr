from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OfferSerializer, OfferDetailSerializer, OfferListSerializer
from offers_app.models import Offer, OfferDetail
from .permissions import IsBusinessUserOrReadOnly
from .filters import OfferFilter

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = [IsAuthenticated, IsBusinessUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfferFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return OfferListSerializer
        return OfferSerializer
    
class OfferDetailView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OfferDetailSerializer
    lookup_field = 'pk' 
