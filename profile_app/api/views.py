from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer , BusinessListSerializer, CustomerListSerializer
from profile_app.models import UserProfile

# Create your views here.
class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'


class BusinessListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessListSerializer
    
    def get_queryset(self):
        return UserProfile.objects.filter(type='business')
    
class CustomerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(type='customer')