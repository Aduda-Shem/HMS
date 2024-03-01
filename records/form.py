# forms.py
from django import forms
from doctors.models import HealthcareProfessional
from records.models import Diagnosis, MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['doctor', 'diagnosis', 'prescription', 'blood_pressure', 'heart_rate', 'temperature', 'weight', 'height', 'medical_history', 'family_history', 'lab_results']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'heart_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control'}),
            'family_history': forms.Textarea(attrs={'class': 'form-control'}),
            'lab_results': forms.Textarea(attrs={'class': 'form-control'}),
        }
