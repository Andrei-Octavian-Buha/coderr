from django.contrib import admin
from .models import Offer, OfferDetail

class OfferDetailInline(admin.TabularInline): # Aceasta este magia
    model = OfferDetail
    extra = 3 # Îți va afișa automat 3 rânduri goale pentru cele 3 pachete
    max_num = 3 # Limitează la maxim 3 detalii per ofertă

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferDetailInline]