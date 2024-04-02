from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from doctors.models import HealthcareProfessional, Patient

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_billed = models.BooleanField(default=False)
   
    def get_full_details(self):
        """
        Returns a string containing the full details of the appointment.
        """
        return f"Appointment with {self.doctor} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}. Purpose: {self.purpose}. Status: {self.status}. Price: {self.price}"
    
class Schedule(models.Model):
    healthcare_professional = models.ForeignKey(HealthcareProfessional, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    data = models.TextField()
