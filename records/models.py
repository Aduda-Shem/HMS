from django.db import models
from patients.models import Patient
from doctors.models import HealthcareProfessional

class FileNumber(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, related_name='file_number')
    number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"File Number {self.number} for {self.patient.first_name} {self.patient.last_name}"

class Diagnosis(models.Model):
    file_number = models.ForeignKey(
        FileNumber, on_delete=models.CASCADE, related_name='diagnoses')
    diagnosis_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Diagnosis for {self.file_number.patient.first_name} {self.file_number.patient.last_name} on {self.diagnosis_date}"

class MedicalRecord(models.Model):
    file_number = models.ForeignKey(
        FileNumber, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(
        HealthcareProfessional, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, related_name='medical_records', null=True, blank=True)
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

class Symptom(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='symptoms')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Symptom '{self.name}' for {self.medical_record.patient.first_name} {self.medical_record.patient.last_name}"

class Allergy(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='allergies')
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return f"Allergy '{self.name}' for {self.medical_record.patient.first_name} {self.medical_record.patient.last_name}"

class Medication(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Medication '{self.name}' for {self.medical_record.patient.first_name} {self.medical_record.patient.last_name}"
