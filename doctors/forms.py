from django import forms
from django.contrib.auth import get_user_model

from doctors.models import HealthcareProfessional, Patient, User
from patients.models import Appointment, Schedule

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
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = HealthcareProfessional
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'specialization']
        
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
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        
        self.fields['patient'].queryset = Patient.objects.all()
        self.fields['doctor'].queryset = HealthcareProfessional.objects.filter(role='doctor') 

    patient = forms.ModelChoiceField(
        queryset=None,  
        empty_label="Select a patient",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    doctor = forms.ModelChoiceField(
        queryset=None,  
        empty_label="Select a doctor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'purpose', 'status', "price"]

        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }



class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'date', 'start_time', 'end_time', 'data']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'data': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter data'}),
        }