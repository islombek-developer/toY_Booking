from django.db import models
from apps.users.models import CustomUser

class Venue(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='venues')
    name = models.CharField(max_length=255)
    description = models.TextField()
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    price_base = models.DecimalField(max_digits=12, decimal_places=2)
    services = models.JSONField(default=dict)
    payment_requirement = models.PositiveIntegerField(default=0, help_text="Oldindan to'lov foizi")
    payment_terms = models.TextField(blank=True, null=True)
    cancellation_policy = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='venues/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.venue.name} - {'Asosiy' if self.is_main else 'Qoshimcha'} rasm"


class VenueAvailability(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='availability')
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    price_override = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    class Meta:
        unique_together = ('venue', 'date')
        
    def __str__(self):
        return f"{self.venue.name} - {self.date} - {'Bosh' if self.is_available else 'Band'}"