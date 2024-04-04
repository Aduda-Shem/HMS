from django.db import models
from patients.models import Patient
from doctors.models import HealthcareProfessional
from django.utils.translation import gettext_lazy as _
import uuid

class FileNumber(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, related_name='file_number')
    number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"File Number {self.number} for {self.patient.first_name} {self.patient.last_name}"

class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Diagnosis: {self.name}"

class MedicalRecord(models.Model):
    file_number = models.ForeignKey(
        FileNumber, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(
        HealthcareProfessional, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, related_name='medical_records', null=True, blank=True)
    prescription = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    heart_rate = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    lab_results = models.TextField(blank=True, null=True)
    total_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    allergies = models.CharField(max_length=20, blank=True, null=True)
    medications = models.TextField(blank=True)
    billed = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"Medical Record for Patient {self.file_number.patient.first_name} {self.file_number.patient.last_name}"

class Symptom(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='symptoms')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Symptom: {self.name}"

class AdmissionCharge(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='admission_charges_records')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Admission Charge: {self.description}"

class Allergy(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='allergies_records')
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return f"Allergy: {self.name}"

class Medication(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='medications_records')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Medication: {self.name}"

class MedicationCharge(models.Model):
    medical_record = models.ForeignKey(
        'MedicalRecord', on_delete=models.CASCADE, related_name='medication_charges_records')
    medication = models.ForeignKey(
        'Medication', on_delete=models.CASCADE, related_name='medication_charges')
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billed = models.BooleanField(null=True, blank=True)
    invoice = models.ForeignKey('Invoice', on_delete=models.SET_NULL, related_name='medication_charges', null=True, blank=True)

    def __str__(self):
        return f"Medication Charge: {self.medication.name}"

class TreatmentCharge(models.Model):
    medical_record = models.ForeignKey(
        'MedicalRecord', on_delete=models.CASCADE, related_name='treatment_charges_records')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billed = models.BooleanField(null=True, blank=True)
    invoice = models.ForeignKey('Invoice', on_delete=models.SET_NULL, related_name='treatment_charges', null=True, blank=True)

    def __str__(self):
        return f"Treatment Charge: {self.description}"



class Invoice(models.Model):
    reference_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    appointment_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Appointment Fee'), default=0)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Admission Fee'), default=0)
    other_fees = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Other Fees'), default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Total Amount'), default=0)
    paid = models.BooleanField(default=False) 
    pending = models.BooleanField(default=True) 

    def __str__(self):
        return f"Invoice - ID: {self.id}, Reference Number: {self.reference_number}"