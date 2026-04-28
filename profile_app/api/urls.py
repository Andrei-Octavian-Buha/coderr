from django.urls import path
from .views import UserProfileDetailView , BusinessListView, CustomerListView

urlpatterns = [
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile-view'),
    path('profiles/business/', BusinessListView.as_view(), name='business-profiles'),
    path('profiles/customer', CustomerListView.as_view(), name='customer-profiles')
]