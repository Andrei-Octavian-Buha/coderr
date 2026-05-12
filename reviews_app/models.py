from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    business_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='reviews_received')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_written')
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =('business_user', 'reviewer')

    def __str__(self):
        return f"{self.reviewer} -> {self.business_user}: {self.rating} stars"