from django.db import models

# Create your models here.
from django.db import models

#Model for the appointment
class Appointment(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Wednesday', 'Wednesday'),
        ('Friday', 'Friday'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_day = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self):
        return f"{self.name}'s appointment on {self.appointment_day}"
