from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

class FileNumber(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='file_number')
    number = models.CharField(max_length=20, unique=True)

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnoses')
    diagnosis_date = models.DateField()
    description = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    doctor = models.CharField(max_length=100)
    purpose = models.TextField()

class Schedule(models.Model):
    doctor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Add other fields as needed
