from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_patient(request):


    context = {
    }

    return render(request, 'patients/add_patient.html', context)

@login_required
def add_appointment(request):


    context = {
    }

    return render(request, 'appointment/add_appointment.html', context)

@login_required
def view_appointment(request):


    context = {
    }

    return render(request, 'appointment/appointments.html', context)