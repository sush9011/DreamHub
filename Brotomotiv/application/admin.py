# Register your models here.
from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')  # Columns to display in the admin panel
    search_fields = ('name', 'email', 'phone')  # Enable search functionality
    list_filter = ('submitted_at',)  # Enable filtering by submission date
    ordering = ('-submitted_at',)  # Order by latest first
