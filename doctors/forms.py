from django import forms
from django.contrib.auth import get_user_model

from doctors.models import HealthcareProfessional, Patient

class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'custom-email-input form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'prompt srch_explore form-control'}))

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = HealthcareProfessional
        fields = ['email', 'first_name', 'last_name', 'license_number']

class AddNurseForm(forms.ModelForm):
    class Meta:
        model = HealthcareProfessional
        fields = ['email', 'first_name', 'last_name','license_number']

class AddHealthcareProfessionalForm(forms.ModelForm):
    class Meta:
        model = HealthcareProfessional
        fields = ['email', 'first_name', 'last_name', 'role', 'specialization']


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'id_number', 'date_of_birth',
                   'gender', 'medical_record_number', 'address', 'phone_number', 'insurance_provider']

    def clean_id_number(self):
        id_number = self.cleaned_data['id_number']
        if len(id_number) != 8:  # Example validation, adjust as needed
            raise forms.ValidationError("ID number must be 8 characters long.")
        return id_number

    def clean_email(self):
        email = self.cleaned_data['email']
        # Example validation to ensure unique email
        if Patient.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
