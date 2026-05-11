from django.urls import path
from rest_framework import routers
from .views import OrderView, OrderCountView, CompleatedOrderCount

router = routers.SimpleRouter()
router.register(r'orders', OrderView, basename='order')
urlpatterns = [
    path('order-count/<int:pk>/', OrderCountView.as_view(), name='order-count'),
    path('completed-order-count/<int:pk>/',  CompleatedOrderCount.as_view(), name='compleated-count')
]
urlpatterns += router.urls