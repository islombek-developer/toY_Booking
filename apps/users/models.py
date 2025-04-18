from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import uuid
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('venue_owner', 'Toyxona egasi'),
        ('customer', 'Mijoz'),
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    telegram_id = models.CharField(max_length=50, blank=True, null=True)
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def check_empty_password(self):
        if not self.username:
            username = f'username-{uuid.uuid4().__str__().split("-")[-1]}'
            
            
        if not self.password:
            password = f'password-{uuid.uuid4().__str__().split("-")[-1]}'
            self.password = password



    def save(self, *args, **kwargs):
        self.check_empty_password()
        self.check_hash_password()
        super(CustomUser, self).save(*args, **kwargs)
