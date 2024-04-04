from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Patient
from records.form import DiagnosisForm, MedicalRecordForm
from records.models import Diagnosis, FileNumber, Invoice, MedicalRecord, MedicationCharge, TreatmentCharge
from django.http import HttpResponse, JsonResponse
from django.db import transaction

# Create your views here.
@login_required
def records(request):
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
        file_number = patient.file_number
        medical_records = MedicalRecord.objects.filter(file_number=file_number)
    except Patient.DoesNotExist:
        medical_records = MedicalRecord.objects.all()

    context = {
        'medical_records': medical_records,
    }

    return render(request, 'records/hospital_records.html', context)

@login_required
def view_record(request, record_id):
    record = get_object_or_404(MedicalRecord, pk=record_id)

    context = {
        'medical_record': record,
    }
    
    return render(request, 'records/view_record.html', context)

@login_required
def view_patient_file(request):
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
        file_record = FileNumber.objects.get(patient=patient)
    except Patient.DoesNotExist:
        return HttpResponse("You are not authorized to view this page.")
    except FileNumber.DoesNotExist:
        file_record = None

    context = {
        'file_data': file_record,
    }

    return render(request, 'patients/view_patient_file.html', context)


def view_all_files(request):
    
    file_records = FileNumber.objects.all()

    context = {
        'file_data': file_records,
    }

    return render(request, 'patients/hospital_file.html', context)

@login_required
def view_file(request, file_number_id):
    file_record = get_object_or_404(FileNumber, id=file_number_id)
    medical_records = file_record.medical_records.all()
    context = {
        'file_data': file_record,
        'medical_records': medical_records,
    }
    return render(request, 'patients/patient_file.html', context)

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

# diagnosis
@login_required
def view_diagnosis(request,):
    diagnosis = Diagnosis.objects.all()
    context = {
        'diagnosis': diagnosis,
    }
    return render(request, 'diagnosis/view_diagnosis.html', context)

@login_required
def add_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_diagnosis')
    else:
        form = DiagnosisForm()
    return render(request, 'diagnosis/view_diagnosis.html', {'form': form})

@login_required
def edit_diagnosis(request, diagnosis_id):
    diagnosis = get_object_or_404(Diagnosis, id=diagnosis_id)
    if request.method == 'POST':
        form = DiagnosisForm(request.POST, instance=diagnosis)
        if form.is_valid():
            form.save()
            return redirect('view_diagnosis')
    else:
        form = DiagnosisForm(instance=diagnosis)
    return render(request, 'diagnosis/view_diagnosis.html', {'form': form})

@login_required
def delete_diagnosis(request, diagnosis_id):
    diagnosis = get_object_or_404(Diagnosis, id=diagnosis_id)
    diagnosis.delete()
    return redirect('view_diagnosis')

@login_required
def create_invoice_from_charges(request):
    try:
        # Retrieve all medication charges and treatment charges where billed is false
        medication_charges = MedicationCharge.objects.filter(billed=False)
        treatment_charges = TreatmentCharge.objects.filter(billed=False)

        # Calculate the total amount for medication charges and treatment charges
        total_medication_charges = sum(charge.amount for charge in medication_charges)
        total_treatment_charges = sum(charge.amount for charge in treatment_charges)

        # Calculate total amount for the invoice
        total_amount = total_medication_charges + total_treatment_charges

        # Create an invoice object with the calculated total amount
        with transaction.atomic():
            invoice = Invoice.objects.create(
                appointment_fee=0,  # Update these fields based on your logic
                admission_fee=0,    # Update these fields based on your logic
                other_fees=total_amount,
                total_amount=total_amount,
                pending=True  # Update this field based on your logic
            )

            # Mark all medication charges as billed and associate them with the invoice
            medication_charges.update(billed=True, invoice=invoice)

            # Mark all treatment charges as billed and associate them with the invoice
            treatment_charges.update(billed=True, invoice=invoice)

        return HttpResponse("Invoice created successfully")
    except Exception as e:
        return HttpResponse("Error occurred while creating invoice: {}".format(e))


def view_invoices(request, status=None):
    try:
        if status == 'paid':
            invoices = Invoice.objects.filter(paid=True)
        elif status == 'pending':
            invoices = Invoice.objects.filter(pending=True)
        else:
            invoices = Invoice.objects.all()

        return render(request, 'patients/invoice.html', {'invoices': invoices})
    except Exception as e:
        return HttpResponse("Error occurred while fetching invoices: {}".format(e))


def update_invoice_status(request, invoice_id, status):
    try:
        invoice = Invoice.objects.get(id=invoice_id)
        if status == 'paid':
            invoice.paid = True
            invoice.pending = False
        elif status == 'pending':
            invoice.paid = False
            invoice.pending = True
        invoice.save()
        return HttpResponse(f"Invoice {invoice_id} status updated to {status}.")
    except Invoice.DoesNotExist:
        return HttpResponse("Invoice does not exist.")