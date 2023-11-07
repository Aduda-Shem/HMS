from django.shortcuts import render

from doctors.forms import CustomUserCreationForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user and user.is_active:
                auth_login(request, user)
                messages.success(request, 'Successfully logged in')
                return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Incorrect credentials.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = LoginForm()

    return render(request, 'users/user_login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, f"Successfully logged out")
    return redirect('login')



def doctor_dashboard(request):

    context = {
    }

    return render(request, 'doctors/doctor_dashboard.html', context)


def add_doctor(request):


    context = {
    }

    return render(request, 'doctors/add_doctor.html', context)


def add_nurse(request):


    context = {
    }

    return render(request, 'nurse/add_nurse.html', context)
