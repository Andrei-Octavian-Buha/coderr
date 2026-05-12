from django.urls import path
from rest_framework import routers
from .views import ReviewView

router = routers.SimpleRouter()
router.register(r'reviews',ReviewView, basename='review')

urlpatterns = router.urls