from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Doctor, Nurse
from .forms import AddDoctorForm, AddNurseForm, LoginForm

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
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                auth_login(request, user)
                messages.success(request, 'Successfully logged in')
                if user.is_doctor:
                    return redirect('doctor_dashboard')
                elif user.is_nurse:
                    return redirect('nurse_dashboard')
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
        print("Doctor: ", form)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            create_user_with_id_password(doctor.id)
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
            nurse = form.save(commit=False)
            nurse.user = request.user
            nurse.save()
            messages.success(request, 'Nurse added successfully')
            return redirect('nurse_dashboard')
    else:
        form = AddNurseForm()
    return render(request, 'nurse/add_nurse.html', {'form': form})
