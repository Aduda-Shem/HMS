from django import forms

from doctors.models import HealthcareProfessional

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
        fields = ['email', 'first_name', 'last_name', 'role', 'specialization', 'license_number', 'date_of_birth', 'gender']