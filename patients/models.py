from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from doctors.models import Patient

class Appointment(models.Model):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    
    STATUS_CHOICES = [
        (PENDING, _('Pending')),
        (IN_PROGRESS, _('In Progress')),
        (COMPLETED, _('Completed')),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    doctor = models.CharField(max_length=100)
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

class Schedule(models.Model):
    doctor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
