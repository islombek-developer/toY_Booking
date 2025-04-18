from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('venue_owner', 'Toyxona egasi'),
        ('customer', 'Mijoz'),
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    telegram_id = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.username