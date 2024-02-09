from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User

from doctors.models import HealthcareProfessional
from .forms import AddDoctorForm, AddHealthcareProfessionalForm, AddNurseForm, LoginForm

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            password = User.objects.make_random_password()
            user = User.objects.create_user(email=email, password=password)
            user.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('doctor_dashboard')
        else:
            messages.error(request, 'Email already exists.')
    return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Pass email as username
            if user is not None and user.is_active:
                auth_login(request, user)
                messages.success(request, 'Successfully logged in')
                if hasattr(user, 'doctor'):  # Check if the user is associated with a Doctor instance
                    return redirect('doctor_dashboard')
                elif hasattr(user, 'nurse'):  # Check if the user is associated with a Nurse instance
                    return redirect('nurse_dashboard')
                else:
                    return redirect('patient_dashboard')  # Redirect to patient dashboard if not a doctor or nurse
            else:
                messages.error(request, 'Incorrect credentials.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = LoginForm()
    return render(request, 'users/user_login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctors/doctor_dashboard.html')

@login_required
def nurse_dashboard(request):
    return render(request, 'nurse/nurse_dashboard.html')

def create_user_with_id_password(license_number):
    password = f'user{license_number}'
    user = User.objects.create_user(username=f'user{license_number}', password=password)
    return user

@login_required
def add_doctor(request):
    if request.method == "POST":
        form = AddDoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()

            user = User.objects.create_user(
                username=doctor.email,
                email=doctor.email,
                password='defaultpassword',
                first_name=doctor.first_name,
                last_name=doctor.last_name
            )

            healthcare_professional = HealthcareProfessional.objects.create(
                user=user,
                email=doctor.email,
                first_name=doctor.first_name,
                last_name=doctor.last_name,
                role='doctor',  
                specialization=doctor.specialization,
                license_number=doctor.license_number,
                date_of_birth=doctor.date_of_birth,
                gender=doctor.gender
            )

            messages.success(request, 'Doctor added successfully')
            return redirect('doctor_dashboard')
    else:
        form = AddDoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})

@login_required
def add_nurse(request):
    if request.method == "POST":
        form = AddNurseForm(request.POST)
        if form.is_valid():
            # Save the nurse information
            nurse = form.save(commit=False)
            nurse.save()

            user = User.objects.create_user(
                username=nurse.email,
                email=nurse.email,
                password='defaultpassword', 
                first_name=nurse.first_name,
                last_name=nurse.last_name
            )

            healthcare_professional = HealthcareProfessional.objects.create(
                user=user,
                email=nurse.email,
                first_name=nurse.first_name,
                last_name=nurse.last_name,
                role='nurse', 
                phone_number=nurse.phone_number,
                license_number=nurse.license_number
            )

            messages.success(request, 'Nurse added successfully')
            return redirect('nurse_dashboard')
    else:
        form = AddNurseForm()
    return render(request, 'nurses/add_nurse.html', {'form': form})



# Self registeration
def add_healthcare_professional(request):
    if request.method == "POST":
        form = AddHealthcareProfessionalForm(request.POST)
        print("FORM:", form.data)
        if form.is_valid():
            print("jkdhasfgcvdastvy")
            healthcare_professional = form.save()
            healthcare_professional.save()

            user_data = form.cleaned_data
            user = User.objects.create_user(
                username=user_data['email'],
                email=user_data['email'],
                password='defaultpassword',
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )

            healthcare_professional_data = form.cleaned_data
            print("heajsbkwdhjv", healthcare_professional_data)
            healthcare_professional_data.pop('email')
            healthcare_professional_data.pop('first_name')
            healthcare_professional_data.pop('last_name')
            healthcare_professional_data['user'] = user

            healthcare_professional = HealthcareProfessional.objects.create(**healthcare_professional_data)

            messages.success(request, 'Healthcare professional added successfully')
            return redirect('healthcare_professional_dashboard')
    else:
        form = AddHealthcareProfessionalForm()
    return render(request, 'users/register.html', {'form': form})