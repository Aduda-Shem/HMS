from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Patient
from records.form import MedicalRecordForm
from records.models import FileNumber, MedicalRecord

# Create your views here.
@login_required
def records(request):
    # Fetch medical records for the logged-in patient if available
    user = request.user
    
    try:
        patient = Patient.objects.get(user=user)
        file_number = patient.file_number
        medical_records = MedicalRecord.objects.filter(file_number=file_number)
    except Patient.DoesNotExist:
        # If patient does not exist, retrieve all medical records
        medical_records = MedicalRecord.objects.all()

    context = {
        'medical_records': medical_records,
    }

    return render(request, 'records/hospital_records.html', context)


@login_required
def file(request):
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
        file_record = FileNumber.objects.get(patient=patient)
    except Patient.DoesNotExist:
        file_record = FileNumber.objects.all()
    except FileNumber.DoesNotExist:
        file_record = None

    context = {
        'file_data': file_record,
    }

    return render(request, 'patients/hospital_file.html', context)

@login_required
def file(request, file_number_id):
    file_record = get_object_or_404(FileNumber, id=file_number_id)
    medical_records = file_record.medical_records.all()
    context = {
        'file_data': file_record,
        'medical_records': medical_records,
    }
    return render(request, 'patients/hospital_file.html', context)

def add_medical_record(request, file_number_id):
    file_record = get_object_or_404(FileNumber, id=file_number_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.file_number = file_record
            medical_record.save()
            return redirect('view_file', file_number_id=file_number_id)
    else:
        form = MedicalRecordForm()
    return render(request, 'patients/add_medical_record.html', {'form': form})

def edit_medical_record(request, medical_record_id):
    medical_record = get_object_or_404(MedicalRecord, id=medical_record_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('view_file', file_number_id=medical_record.file_number.id)
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'patients/edit_medical_record.html', {'form': form})

def delete_medical_record(request, medical_record_id):
    medical_record = get_object_or_404(MedicalRecord, id=medical_record_id)
    file_number_id = medical_record.file_number.id
    medical_record.delete()
    return redirect('view_file', file_number_id=file_number_id)
