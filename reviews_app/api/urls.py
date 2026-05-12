from django.urls import path
from rest_framework import routers
from .views import ReviewView , BaseInfoView

router = routers.SimpleRouter()
router.register(r'reviews',ReviewView, basename='review')

urlpatterns = [
    path('base-info/', BaseInfoView.as_view(), name='base-info')
]
urlpatterns += router.urls