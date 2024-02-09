from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from records.models import MedicalRecord

# Create your views here.
@login_required
def records(request):
    # Fetch medical records for the logged-in patient
    medical_records = MedicalRecord.objects.filter(patient=request.user.patient)

    context = {
        'medical_records': medical_records,
    }

    return render(request, 'records/hospital_records.html', context)