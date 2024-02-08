from django.shortcuts import render

# Create your views here.
def add_patient(request):


    context = {
    }

    return render(request, 'patients/add_patient.html', context)

def add_appointment(request):


    context = {
    }

    return render(request, 'appointment/add_appointment.html', context)

def view_appointment(request):


    context = {
    }

    return render(request, 'appointment/appointments.html', context)