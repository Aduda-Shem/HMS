from django.db import models
from patients.models import Patient
from doctors.models import HealthcareProfessional

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(HealthcareProfessional, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    heart_rate = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    family_history = models.TextField(blank=True, null=True)
    lab_results = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name}"

    def get_patient_full_name(self):
        return f"{self.patient.first_name} {self.patient.last_name}"

    def get_doctor_full_name(self):
        return f"{self.doctor.first_name} {self.doctor.last_name}"

    def get_date_created(self):
        return self.date_created.strftime("%Y-%m-%d %H:%M:%S")

    def get_date_updated(self):
        return self.date_updated.strftime("%Y-%m-%d %H:%M:%S")

class Symptom(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='symptoms')
    name = models.CharField(max_length=100)

class Allergy(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='allergies')
    name = models.CharField(max_length=100)

class Medication(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
