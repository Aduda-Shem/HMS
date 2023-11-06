from django.shortcuts import render

# Create your views here.


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
