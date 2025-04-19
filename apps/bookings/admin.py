from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('venue', 'customer', 'booking_date', 'guest_count', 'status', 'created_at')
    list_filter = ('status', 'booking_date')
    search_fields = ('venue__name', 'customer__username')