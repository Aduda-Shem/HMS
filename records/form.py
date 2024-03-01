from django import forms
from doctors.models import HealthcareProfessional

from records.models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=HealthcareProfessional.objects.all(), required=True)
    diagnosis = forms.CharField(max_length=100, required=True)
    prescription = forms.CharField(widget=forms.Textarea, required=True)
    blood_pressure = forms.CharField(max_length=20, required=False)
    heart_rate = forms.CharField(max_length=20, required=False)

    class Meta:
        model = MedicalRecord
        fields = ['doctor', 'diagnosis', 'prescription', 'blood_pressure', 'heart_rate']