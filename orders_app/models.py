from django.db import models
from django.conf import settings
from offers_app.models import OfferDetail


# Create your models here.
class Order(models.Model):
    class StatusType(models.TextChoices):
        IN_PROGRESS = "in_progress","In Progress"
        COMPLETED = "completed","Completed"
        CANCELLED = "cancelled","Cancelled"
    class OfferType(models.TextChoices):
        BASIC = "basic","Basic"
        STANDARD = "standard","Standard"
        PREMIUM = "premium","Premium"
    customer_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bought_orders')
    business_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_orders')
    offer_detail = models.ForeignKey(OfferDetail, on_delete=models.CASCADE,related_name='details')
    title = models.CharField(max_length=255)
    revisions = models.PositiveIntegerField(default=1)
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    features = models.JSONField(default=list)
    offer_type = models.CharField(max_length=20, choices=OfferType.choices,default=OfferType.STANDARD)
    status = models.CharField(max_length=20, choices=StatusType.choices, default=StatusType.IN_PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)