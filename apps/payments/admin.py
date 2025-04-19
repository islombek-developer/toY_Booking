from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_type', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_type', 'payment_method')
    search_fields = ('booking__venue__name', 'booking__customer__username', 'transaction_id')