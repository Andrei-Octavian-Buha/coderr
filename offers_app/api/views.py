from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Min
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import OfferSerializer, OfferDetailSerializer, OfferListSerializer, OfferRetrieveSerializer
from offers_app.models import Offer, OfferDetail
from .permissions import IsBusinessUserOrReadOnly
from .filters import OfferFilter
from .pagination import StandardResultsSetPagination

class OfferView(viewsets.ModelViewSet):
    """
    ViewSet for managing business offers.
    
    Provides standard lifecycle operations for offers. It calculates the 
    minimum price dynamically for sorting and filtering purposes. 
    Access is restricted: only business users can create or modify offers, 
    while others have read-only access.
    """
    queryset = Offer.objects.annotate(min_price=Min('details__price'),min_delivery_time=Min('details__delivery_time_in_days')).distinct().all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OfferFilter
    ordering_fields = ['updated_at', 'min_price']
    search_fields = ['title','description']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return OfferListSerializer
        if self.action == 'retrieve':
            return OfferRetrieveSerializer
        return OfferSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        return [IsBusinessUserOrReadOnly()]
    

class OfferDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a specific offer detail package.
    
    Provides in-depth information about a single pricing tier or 
    service package associated with an offer.
    """
    queryset = OfferDetail.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OfferDetailSerializer
    lookup_field = 'pk' 
