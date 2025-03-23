from django import forms
from .models import ServiceBooking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'service_type', 'appointment_date', 'message']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            
        }
