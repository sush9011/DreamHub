from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)  # Name field
    email = models.EmailField(unique=True)   # Email field
    phone = models.CharField(max_length=15, unique=True)  # Phone number field
    message = models.TextField()  # Message field
    submitted_at = models.DateTimeField(auto_now_add=True)  # Auto-timestamp

    def __str__(self):
        return f"{self.name} - {self.email}"
