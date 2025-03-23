from django.db import models

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#form for service booking
class ServiceBooking(models.Model):
    SERVICE_CHOICES = [
        ('ppf', 'Paint Protection Film'),
        ('wrap', 'Car Wrapping'),
        ('detail', 'Car Detailing'),
        ('mod', 'Car Modification'),
        ('repair', 'Accidental Repair')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()}"

