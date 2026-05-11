from rest_framework import viewsets, generics

class OrderView(viewsets.ModelViewSet):
    pass

class OrderCountView(generics.RetrieveAPIView):
   pass

class CompleatedOrderCount(generics.RetrieveAPIView):
   pass
