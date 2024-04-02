# forms.py
from django import forms
from records.models import AdmissionCharge, Allergy, Diagnosis, MedicalRecord, Medication, MedicationCharge, Symptom, TreatmentCharge

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['doctor', 'diagnosis', 'prescription', 'blood_pressure', 'heart_rate', 'temperature', 'weight', 'height', 'lab_results']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'heart_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'lab_results': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AdmissionChargeForm(forms.ModelForm):
    class Meta:
        model = AdmissionCharge
        fields = ['description', 'amount']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TreatmentChargeForm(forms.ModelForm):
    class Meta:
        model = TreatmentCharge
        fields = ['description', 'amount']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MedicationChargeForm(forms.ModelForm):
    class Meta:
        model = MedicationCharge
        fields = ['medication', 'quantity', 'amount']
        widgets = {
            'medication': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }