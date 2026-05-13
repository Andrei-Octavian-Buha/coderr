from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import viewsets, views
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter
from reviews_app.models import Review
from orders_app.models import Order 
from offers_app.models import Offer 
from .permissions import IsCustomerUserOrReadOnly, IsReviewOwner
from .serializers import ReviewSerializer, UpdateReviewSerializer
from .filters import ReviewFilter
from rest_framework.response import Response

User = get_user_model()

class ReviewView(viewsets.ModelViewSet):
    """
    ViewSet for managing service reviews.
    
    Provides functionality to list, create, and manage reviews. 
    It features custom permission logic where only customers can create reviews, 
    and only the author can modify or delete their own feedback. 
    Includes advanced filtering and ordering by rating or date.
    """
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReviewFilter
    ordering_fields = ['updated_at', 'rating']
    pagination_class = None

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


class BaseInfoView(views.APIView):
    """
    Public API view for global platform statistics.
    
    Provides aggregate data including total review count, platform-wide 
    average rating, number of registered business profiles, and total 
    active offers. Access is open to everyone (AllowAny).
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        review_count = Review.objects.count()

        avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
        average_rating = round(avg_rating or 0.0,1)

        business_profile_count = User.objects.filter(profile__type='business').count()
        
        offer_count = Offer.objects.count()

        return Response({
            "review_count": review_count,
            "average_rating": average_rating,
            "business_profile_count": business_profile_count,
            "offer_count": offer_count
        })