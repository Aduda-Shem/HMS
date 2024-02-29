from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from doctors.forms import AddPatientForm, AppointmentForm
from doctors.models import Patient
from patients.forms import FileNumberForm

from patients.models import Appointment
from django.contrib.auth import get_user_model
from django.contrib import messages

from records.models import FileNumber

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
            user.set_password(user_data['id_number'])
            user.save()  # Save the user with the password
            
            try:
                patient_data = {
                    'user': user,
                    'id_number': user_data['id_number'],
                    'medical_record_number': user_data['medical_record_number'],
                    'date_of_birth': user_data['date_of_birth'],
                    'gender': user_data['gender'],
                    'address': user_data['address'],
                    'phone_number': user_data['phone_number'],
                    'insurance_provider': user_data['insurance_provider'],
                }
                patient = Patient.objects.create(**patient_data)
                
                # Create FileNumber with the same number as the ID number
                file_number = FileNumber.objects.create(patient=patient, number=user_data['id_number'])
                
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
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments') 
    else:
        form = AppointmentForm()
    
    context = {'form': form}
    return render(request, 'appointment/add_appointments.html', context)

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

    if new_status in [Appointment.IN_PROGRESS, Appointment.COMPLETED]:
        appointment.status = new_status
        appointment.save()
    else:
        pass

    return redirect('view_appointment')

