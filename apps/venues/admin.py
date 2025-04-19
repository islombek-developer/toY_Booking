from django.contrib import admin
from .models import Venue, VenueImage, VenueAvailability

class VenueImageInline(admin.TabularInline):
    model = VenueImage
    extra = 1
    
class VenueAvailabilityInline(admin.TabularInline):
    model = VenueAvailability
    extra = 1

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'district', 'owner', 'capacity', 'price_base', 'payment_requirement', 'is_active')
    list_filter = ('region', 'is_active')
    search_fields = ('name', 'region', 'district', 'owner__username')
    inlines = [VenueImageInline, VenueAvailabilityInline]

@admin.register(VenueImage)
class VenueImageAdmin(admin.ModelAdmin):
    list_display = ('venue', 'image', 'is_main', 'created_at')
    list_filter = ('is_main', 'created_at')
    search_fields = ('venue__name',)

@admin.register(VenueAvailability)
class VenueAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('venue', 'date', 'is_available', 'price_override')
    list_filter = ('is_available', 'date')
    search_fields = ('venue__name',)