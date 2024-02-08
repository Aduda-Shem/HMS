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
from patients.views import add_appointment, view_appointment, add_patient

from doctors import views
from records.views import records

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/', admin.site.urls), 
    path('', views.doctor_dashboard, name='doctor_dashboard'),

    # Dashboard
    path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),
    path('nurse_dashboard', views.nurse_dashboard, name='nurse_dashboard'),

    # adding new users and appointment and schedules
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('add_nurse', views.add_nurse, name='add_nurse'),
    path('add_patient', add_patient, name='add_patient'),
    path('add_appointment', add_appointment, name='add_appointment'),

    # Records
    path('records', records, name='records'),
    path('appointments', view_appointment, name='appointments')





]