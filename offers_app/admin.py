from django.contrib import admin
from .models import Offer, OfferDetail

class OfferDetailInline(admin.TabularInline): 
    model = OfferDetail
    extra = 3 
    max_num = 3 

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferDetailInline]