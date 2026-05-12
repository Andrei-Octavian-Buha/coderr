from django.conf import settings
from django.db.models import Q
from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderUpdateSerializer
from .permissions import IsCustomerOrReadOnly, IsBusinessUserOwner
from orders_app.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderView(viewsets.ModelViewSet):
   def get_permissions(self):
      if self.action == 'destroy':
         return [IsAdminUser()]
      
      if self.action in ['update','partial_update']:
         return [IsBusinessUserOwner()]
      
      return [IsCustomerOrReadOnly()]

   def get_serializer_class(self):
      if self.action in ['update','partial_update']:
         return OrderUpdateSerializer
      return OrderSerializer
   
   def get_queryset(self):
      user = self.request.user
      return Order.objects.filter(
         Q(customer_user=user) | Q(business_user=user)
      ).order_by('-created_at')

class OrderCountView(views.APIView):
   permission_classes = [IsAuthenticated]
   def get(self,request, pk):
      try:
         business_user = User.objects.get(pk=pk,profile__type='business')
      except User.DoesNotExist:
         return Response(
            {"error": "Business user not found."}, 
                status=status.HTTP_404_NOT_FOUND
         )
      
      count = Order.objects.filter(
         business_user = business_user,
         status='in_progress'
      ).count()
      return Response({"order_count": count}, status=status.HTTP_200_OK)

class CompleatedOrderCountView(views.APIView):
   permission_classes = [IsAuthenticated]

   def get(self,request, pk):
      try:
         business_user = User.objects.get(pk=pk, profile__type='business')
      except User.DoesNotExist:
         return Response(
            {"error": "Business user not found."},
            status=status.HTTP_404_NOT_FOUND
         )
      
      count = Order.objects.filter(
         business_user = business_user,
         status = 'completed'
      ).count()
      return Response({"completed_order_count":count}, status=status.HTTP_200_OK)