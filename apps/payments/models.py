from django.db import models
from apps.bookings.models import Booking

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ('advance', 'Oldindan to\'lov'),
        ('full', 'To\'liq to\'lov'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Kutilmoqda'),
        ('successful', 'Muvaffaqiyatli'),
        ('failed', 'Muvaffaqiyatsiz'),
    )
    
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.booking} - {self.amount} - {self.status}"