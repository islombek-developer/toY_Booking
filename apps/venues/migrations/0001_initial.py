# Generated by Django 5.2 on 2025-04-19 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('region', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('capacity', models.PositiveIntegerField()),
                ('price_base', models.DecimalField(decimal_places=2, max_digits=12)),
                ('services', models.JSONField(default=dict)),
                ('payment_requirement', models.PositiveIntegerField(default=0, help_text="Oldindan to'lov foizi")),
                ('payment_terms', models.TextField(blank=True, null=True)),
                ('cancellation_policy', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VenueImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='venues/')),
                ('is_main', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='venues.venue')),
            ],
        ),
        migrations.CreateModel(
            name='VenueAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
                ('price_override', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='venues.venue')),
            ],
            options={
                'unique_together': {('venue', 'date')},
            },
        ),
    ]
