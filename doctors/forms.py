from django import forms
from django.contrib.auth.forms import AuthenticationForm

from doctors.models import Doctor, Nurse

class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'custom-email-input form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'prompt srch_explore form-control'}))

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'email', 'license_number', 'date_of_birth', 'gender']

class AddNurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['first_name', 'last_name', 'email', 'phone', 'assigned_doctor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_doctor'].queryset = Doctor.objects.all() 