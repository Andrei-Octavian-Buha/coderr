from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer , BusinessListSerializer, CustomerListSerializer
from profile_app.models import UserProfile

# Create your views here.
class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve or update a specific user profile.
    
    Allows authenticated users to view any profile, but restricts update 
    permissions exclusively to the profile owner.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'


class BusinessListView(generics.ListAPIView):
    """
    API view to retrieve a list of all business profiles.
    
    Returns a collection of user profiles filtered by the 'business' type, 
    optimized for browsing available service providers.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessListSerializer
    pagination_class = None
    def get_queryset(self):
        return UserProfile.objects.filter(type='business')
    
class CustomerListView(generics.ListAPIView):
    """
    API view to retrieve a list of all customer profiles.
    
    Returns a collection of user profiles filtered by the 'customer' type.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerListSerializer
    pagination_class = None
    def get_queryset(self):
        return UserProfile.objects.filter(type='customer')