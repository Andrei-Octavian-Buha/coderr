from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

class UserProfile(models.Model):
    class TypeChoices(models.TextChoices):
        BUSINESS = "business", "Business"
        CUSTOMER = "customer", "Customer"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    file = models.FileField(upload_to='profiles/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, default="")
    tel = models.CharField(max_length=15, blank=True, default="")
    description = models.CharField(max_length=255, blank=True, default="")
    working_hours = models.CharField(max_length=20, blank=True, default="")
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)




