from django.db import models
from apps.users.models import CustomUser
from apps.venues.models import Venue

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Kutilmoqda'),
        ('confirmed', 'Tasdiqlangan'),
        ('canceled', 'Bekor qilingan'),
        ('completed', 'Bajarilgan'),
    )
    
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    event_type = models.CharField(max_length=100, blank=True, null=True)
    guest_count = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.venue.name} - {self.booking_date} - {self.customer.username}"