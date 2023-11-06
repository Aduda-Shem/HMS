from django.shortcuts import render

# Create your views here.
def add_patient(request):


    context = {
    }

    return render(request, 'patients/add_patient.html', context)
