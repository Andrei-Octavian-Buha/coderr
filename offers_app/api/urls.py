from django.urls import path, include
from rest_framework import routers
from .views import OfferView, OfferDetailView


router = routers.SimpleRouter()
router.register(r'offers', OfferView, basename='offer')

# api/offerdetails/{id}/

urlpatterns = [
    path('offerdetails/<int:pk>/', OfferDetailView.as_view(), name='offer-package-detail')
    ]
urlpatterns += router.urls