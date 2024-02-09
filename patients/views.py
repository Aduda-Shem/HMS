from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from doctors.forms import AddPatientForm
from doctors.models import Patient

from patients.models import Appointment
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
@login_required
def add_patient(request):
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            user.set_password(user_data['id_number'])  # Set password as medical record number
            user.save()  # Save the user with the password
            patient_data = {
                'user': user,
                'id_number': user_data['id_number'],  # Assuming medical_record_number corresponds to id_number in the Patient model
                'medical_record_number': user_data['medical_record_number'],  # Assuming medical_record_number corresponds to id_number in the Patient model
                'date_of_birth': user_data['date_of_birth'],
                'gender': user_data['gender'],
                'address': user_data['address'],
                'phone_number': user_data['phone_number'],
                'insurance_provider': user_data['insurance_provider'],
            }
            try:
                patient = Patient.objects.create(**patient_data)
                messages.success(request, 'Patient added successfully')
                return redirect('patients')
            except Exception as e:
                error_message = f"Error occurred while saving patient: {e}"
                print(error_message)
                messages.error(request, error_message)
        else:
            error_message = "Form is not valid."
            print(form.errors)
            messages.error(request, error_message)
    else:
        form = AddPatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})



@login_required
def view_patients(request):
    patients = Patient.objects.all()

    context = {
        'patients': patients,
    }

    return render(request, 'patients/view_patients.html', context)

@login_required
def add_appointment(request):


    context = {
    }

    return render(request, 'appointment/add_appointment.html', context)

@login_required
def view_appointment(request):
    pending_appointments = Appointment.objects.filter(status='pending')
    in_progress_appointments = Appointment.objects.filter(status='in_progress')
    completed_appointments = Appointment.objects.filter(status='completed')

    context = {
        'pending_appointments': pending_appointments,
        'in_progress_appointments': in_progress_appointments,
        'completed_appointments': completed_appointments,
    }

    return render(request, 'appointment/appointments.html', context)

@login_required
def change_appointment_status(request, appointment_id, new_status):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    appointment.status = new_status
    appointment.save()

    return redirect('view_appointment')