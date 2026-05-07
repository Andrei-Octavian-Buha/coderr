from django.db import models

# Create your models here.

class Offer(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='offers/', blank=True, null=True)
    description = models.TextField(max_length=2000)

class OfferDetail(models.Model):
    class OfferType(models.TextChoices):
        BASIC = "basic","Basic"
        STANDARD = "standard","Standard"
        PREMIUM = "premium","Premium"

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE,related_name='details')
    title = models.CharField(max_length=255)
    revisions = models.PositiveIntegerField(default=1)
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    features = models.JSONField(default=list)
    offer_type = models.CharField(max_length=20, choices=OfferType.choices,default=OfferType.STANDARD)