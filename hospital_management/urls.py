"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from patients.views import add_appointment, change_appointment_status, view_appointment, add_patient, view_patients

from doctors import views
from records.views import add_diagnosis, add_medical_record, delete_diagnosis, delete_medical_record, edit_diagnosis, edit_medical_record, records, view_all_files, view_diagnosis, view_file, view_patient_file, view_record

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),
    path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),

    # Dashboard
    path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),
    path('nurse_dashboard', views.nurse_dashboard, name='nurse_dashboard'),
    path('patient_dashboard', views.patient_dashboard, name='patient_dashboard'),

    # adding new users and appointment and schedules
    path('register', views.add_healthcare_professional, name='register'),

    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('list_doctor', views.view_doctors, name='list_doctors'),

    path('add_nurse', views.add_nurse, name='add_nurse'),
    path('list_nurses', views.view_nurses, name='list_nurses'),

    path('add_patient', add_patient, name='add_patient'),
    path('list_patients', view_patients, name='list_patients'),
    path('add_appointment', add_appointment, name='add_appointment'),

    # Records
    path('records', records, name='records'),
    path('records/<int:record_id>/', view_record, name='view_record'),

    # file
    path('file', view_all_files, name='view_file'),
    path('patient_file', view_patient_file, name='patient_file'),
    path('file/<int:file_number_id>/', view_file, name='view_file'),
    path('file/<int:file_number_id>/add/', add_medical_record, name='add_medical_record'),
    path('medical-record/<int:medical_record_id>/edit/', edit_medical_record, name='edit_medical_record'),
    path('medical-record/<int:medical_record_id>/delete/', delete_medical_record, name='delete_medical_record'),


    path('appointments/', view_appointment, name='appointments'),
    path('appointments/<int:appointment_id>/<str:new_status>/', change_appointment_status, name='change_appointment_status'),

    # diagnosis
    path('diagnosis', view_diagnosis, name='view_diagnosis'),
    path('diagnosis/add/', add_diagnosis, name='add_diagnosis'),
    path('diagnosis/<int:diagnosis_id>/edit/', edit_diagnosis, name='edit_diagnosis'),
    path('diagnosis/<int:diagnosis_id>/delete/', delete_diagnosis, name='delete_diagnosis'),

]