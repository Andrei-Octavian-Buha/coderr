from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from reviews_app.models import Review
from .permissions import IsCustomerUserOrReadOnly, IsReviewOwner
from .serializers import ReviewSerializer, UpdateReviewSerializer
from .filters import ReviewFilter

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReviewFilter
    ordering_fields = ['updated_at', 'rating']

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UpdateReviewSerializer
        return ReviewSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsReviewOwner()]
        return [IsCustomerUserOrReadOnly()]
    
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
